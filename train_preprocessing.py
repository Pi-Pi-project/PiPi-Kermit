import os
import re
import numpy as np
import pandas as pd
from eunjeon import Mecab
from DB_connect_setting import DB
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"
from DB_train_get_data import _user_skill, _user_search_log, _user_view_log, _other_view_log

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
    view_log_df = _user_view_log(email)
    other_view_log_df = _other_view_log(email)
    # try:
    #     skill_df = _user_skill(email)
    #     search_log_df = _user_search_log(email)
    #     view_log_df = _user_view_log(email)
    #     other_view_log_df = _other_view_log(email)
    #
    # finally:
    #     DB.close()

    return skill_df, search_log_df, view_log_df, other_view_log_df

def processed_data(email):
    # US: User_Skillset - user_skill
    # USL: User_Search_Log - search_log
    # UVL: User_View_Log - id, title, skillset, content, view_log, label
    # OVL: Other_USer_Log - id, title, skillset, content, view_log, label
    US, USL, UVL, OVL = get_data(email)

    US.user_skill = lower(US.user_skill)
    USL.search_log = lower(USL.search_log)
    UVL.id = list(map(str, UVL.id))
    UVL.title = nouns(regex(lower(UVL.title)))
    UVL.skillset = lower(UVL.skillset)
    UVL.content = nouns(regex(lower(UVL.content)))
    UVL.view_log = lower(UVL.view_log)
    OVL.id = list(map(str, OVL.id))
    OVL.title = nouns(regex(lower(OVL.title)))
    OVL.skillset = nouns(regex(lower(OVL.title)))
    OVL.content = nouns(regex(lower(OVL.content)))
    OVL.view_log = lower(OVL.view_log)

    train_data_A = pd.concat([US, USL], axis=1, ignore_index=True)
    train_data_B = pd.concat([UVL, OVL], ignore_index=True)
    train_dataset = pd.concat([train_data_A, train_data_B], axis=1, ignore_index=True).sample(frac=1).reset_index(drop=True)
    train_dataset.columns = ["user_skill", "search_log", "id", "title", "skillset", "content", "view_log", "label"]
    train_dataset = train_dataset.fillna("undefined")

    X_sum = []
    X_token = []
    X_raw = train_dataset[[x for x in train_dataset.columns if x != "label"]]
    Y_data = np.array(train_dataset["label"])

    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences

    tokenizer = Tokenizer(oov_token="undefined")

    for idx in range(len(X_raw)):
        loc = list(X_raw.loc[idx])
        tokenizer.fit_on_texts(loc)
        X_token.append(list(tokenizer.texts_to_sequences(loc)))

    for idx in range(len(X_token)):
        loc = sum(X_token[idx], [])
        X_sum.append(loc)

    max_len = 50
    input_dim = len(tokenizer.word_index) + 1
    X_data = np.array(pad_sequences(X_sum, maxlen=max_len, padding="post"))

    # print(X_data)
    # print(X_data.shape)

    return input_dim, max_len, X_data, Y_data