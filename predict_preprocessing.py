import os
import re
import numpy as np
import pandas as pd
from eunjeon import Mecab
from DB_connect_setting import DB
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"
from DB_predict_get_data import _user_skill, _user_search_log, _post_list

# Preprocessing Functions
def regex(input_data):
    result = []

    for text in input_data:
        result.append(re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣0-9a-zA-Z ]', '', text))

    return result

def lower(input_data):
    result = []

    for text in input_data:
        result.append(text.lower())

    return result

def nouns(input_data):
    stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과',
                 '도', '를', '으로', '자', '에', '와', '한', '하다']
    result = []
    mecab = Mecab()

    for text in input_data:
        token = mecab.nouns(text)
        token = [t for t in token if t not in stopwords]
        token = [t for t in token if len(token) > 1]
        token = " ".join(token)
        result.append(token)

    return result

# Get DataFrame from PiPi MySQL DB with PyMySQL
def get_data(email):
    skill_df = _user_skill(email)
    search_log_df = _user_search_log(email)
    post_df = _post_list(email)
    # try:
    #     skill_df = _user_skill(email)
    #     search_log_df = _user_search_log(email)
    #     post_df = _post_list(email)
    #
    # finally:
    #     DB.close()

    return skill_df, search_log_df, post_df

def processed_data(email):
    # US: User_Skillset - user_skill
    # USL: User_Search_Log - search_log
    # PL: Post_List - id, title, skillset, content, view_log
    US, USL, PL = get_data(email)

    # select post.id as 'id', post.title as 'title', post.img as 'img'
    # post.category as 'cate', post.idea as 'idea', post_skillset.skill as 'skillset'
    # post.max as 'max', post.user_email as 'email', user.profile_image as 'profile_img'
    # user.nickname as 'nickname', post.created_at as 'created'
    # post.content as 'content', user_view_log.log as 'view_log'
    predict_PL = PL[[x for x in PL.columns if x not in ["img", "cate", "idea", "max", "email", "profile_img", "nickname", "created"]]]
    response_PL = PL[[x for x in PL.columns if x not in ["content", "view_log"]]]

    US.user_skill = lower(US.user_skill)
    USL.search_log = lower(USL.search_log)
    predict_PL.id = list(map(str, predict_PL.id))
    predict_PL.title = nouns(regex(lower(predict_PL.title)))
    predict_PL.skillset = nouns(regex(lower(predict_PL.skillset)))
    predict_PL.content = nouns(regex(lower(predict_PL.content)))
    predict_PL.view_log = lower(predict_PL.view_log)

    train_data_A = pd.concat([US, USL], axis=1, ignore_index=True)
    train_dataset = pd.concat([train_data_A, predict_PL], axis=1, ignore_index=True).sample(frac=1).reset_index(drop=True)
    train_dataset.columns = ["user_skill", "search_log", "id", "title", "skillset", "content", "view_log"]
    train_dataset = train_dataset.fillna("undefined")

    X_sum = []
    X_token = []

    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences

    tokenizer = Tokenizer(oov_token="undefined")

    for idx in range(len(train_dataset)):
        loc = list(train_dataset.loc[idx])
        tokenizer.fit_on_texts(loc)
        X_token.append(list(tokenizer.texts_to_sequences(loc)))

    for idx in range(len(X_token)):
        loc = sum(X_token[idx], [])
        X_sum.append(loc)

    max_len = 50
    # input_dim = len(tokenizer.word_index) + 1
    X_data = np.array(pad_sequences(X_sum, maxlen=max_len, padding="post"))

    return X_data, response_PL