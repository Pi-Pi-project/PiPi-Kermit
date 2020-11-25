import re
import pandas as pd
import tensorflow as tf
from eunjeon import Mecab
from DB_connect_setting import DB
from DB_get_data import _user_skill, _user_search_log, _user_view_log, _other_view_log
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import *
from tensorflow.keras.models import Sequential, load_model, Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint,  ReduceLROnPlateau
from tensorflow.keras.regularizers import *
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam, RMSprop
# tf.random.set_seed(777)

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

def get_data(email):
    try:
        skill_df = _user_skill(email)
        search_log_df = _user_search_log(email)
        view_log_df = _user_view_log(email)
        other_view_log_df = _other_view_log(email)

    finally:
        DB.close()

    return skill_df, search_log_df, view_log_df, other_view_log_df

# Test Email
email = "a@gmail.com"

# US: User_Skillset - user_skill
# USL: User_Search_Log - search_log
# UVL: User_View_Log - id, title, skillset, content, view_log
# OVL: Other_USer_Log - id, title, skillset, content, view_log
US, USL, UVL, OVL = get_data(email)

US.user_skill = lower(US.user_skill)
USL.search_log = lower(USL.search_log)
UVL.title = nouns(regex(lower(UVL.title)))
UVL.skillset = lower(UVL.skillset)
UVL.content = nouns(regex(lower(UVL.content)))
UVL.view_log = lower(UVL.view_log)
OVL.title = nouns(regex(lower(OVL.title)))
OVL.skillset = lower(OVL.title)
OVL.content = nouns(regex(lower(OVL.content)))
OVL.view_log = lower(OVL.view_log)

# print(UVL.head())
# print(OVL.head())

# Train dataset with label
train_dataset = pd.concat([UVL, OVL]).sample(frac=1).reset_index(drop=True)
train_X_raw = train_dataset[[x for x in train_dataset.columns if x != "label"]]
train_X = []
train_Y = train_dataset["label"]

# print(train_X_raw.head())

for index in list(train_X_raw.columns):
    train_X.append(list(train_X_raw[index]))

print(train_X)

# vocab_size = 5
# tokenizer = Tokenizer(num_words=vocab_size+2, oov_token='OOV')
#
# for data in train_X[2:5]:
#     tokenizer.fit_on_texts(data)