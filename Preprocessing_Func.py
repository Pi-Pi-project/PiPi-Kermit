import re
from eunjeon import Mecab
from DB_connect_setting import DB
from DB_get_data import _user_skill, _user_search_log, _user_view_log

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

    finally:
        DB.close()

    return skill_df, search_log_df, view_log_df