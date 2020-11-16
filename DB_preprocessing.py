import re
from DB_connect_setting import DB
from DB_get_data import _user_skill, _user_search_log, _user_view_log
from eunjeon import Mecab

"""
tensorflow.keras.preprocessing.Tokenizer을 이용하여 특수 문자 제거 및 소문자화가 가능하여
최적화 및 코드의 가독성을 위해서 사용하지 않음

# 특수문자 제거를 위한 정규 표현식
def regex(texts):
    result = []

    for text in texts:
        result.append(re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣0-9a-zA-Z ]', '', text))

    return result

def lower(texts):
    result = []

    for text in texts:
        result.append(str(text).lower())

    return result
"""

def morphs_stopword(texts):
    STOP_WORDS = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과',
                  '도', '를', '으로', '자', '에', '와', '한', '하다']
    mecab = Mecab()
    result = []

    for text in texts:
        tmp = mecab.morphs(text)

        if tmp not in STOP_WORDS:
            result.append(tmp)

    return result

def processed_data(email):
    try:
        # Get Data from MySQL DB
        skill_df = _user_skill(email)
        search_log_df = _user_search_log(email)
        view_log_df = _user_view_log(email)

    finally:
        # Close the connection from the MySQL DB
        DB.close()

    # Convert DataFrame to list
    # 최신의 로그 5개를 추출
    skill_list = list(skill_df["user_skill"])
    search_log_list = list(search_log_df["search_log"].iloc[0:5])
    view_log_list = list(view_log_df["view_log"].iloc[0:5])
    # 분석 시 오류를 줄이고 정확도를 늘리기 위해 추가적인 전처리 진행
    view_title_list = morphs_stopword(view_log_df["title"].iloc[0:5])
    view_content_list = morphs_stopword(view_log_df["post_content"].iloc[0:5])

    # 최신순을 기준으로 오름차순 정렬하기 위해서 reverse 적용
    search_log_list.reverse()
    view_title_list.reverse()
    view_content_list.reverse()
    view_log_list.reverse()

    return skill_list, search_log_list, view_title_list, view_content_list, view_log_list

# Test Email
# email = "a@gmail.com"

# Test Output
# print("========================[Test Output]========================")
# SL, SLL, VTL, VCL, VLL = processed_data(email)
# print("[SL]\n", SL, "\n")
# print("[SLL]\n", SLL, "\n")
# print("[VTL]\n", VTL, "\n")
# print("[VCL]\n", VCL, "\n")
# print("[VLL]\n", VLL, "\n")