import re
from eunjeon import Mecab
mecab = Mecab()

sentence = "20일 0시 기준 코로나19 신규 확진자는 363명. 사흘 연속 300명을 넘었다. 서울 경기 등 수도권 확산세가 걷잡을 수 없다. 21일 중등교사임용시험을 앞두고 이날 서울 동작구 노량진의 한 대형 학원과 관련해 최소 39명의 확진자가 나왔다. 임용시험 응시자는 전국적으로 6만 명이 넘는다. 2주도 남지 않은 대학수학능력시험 방역에 대한 불안감도 커지고 있다."

# 1. 표제어 추출(Lemmatization)
print("품사 태깅 - PoS\n" + str(mecab.pos(sentence)) + "\n")
print("품사 태깅 - Morphs\n" + str(mecab.morphs(sentence)) + "\n")
print("품사 태깅 - Nouns\n" + str(mecab.nouns(sentence)) + "\n")
print("======================================================")

# 2. 불용어 제거(Stopwords Removing)
def text_preprocessing(text, tokenizer):
    STOPWORDS = ['을', '를', '이', '가', '은', '는']

    txt = re.sub("[^가-힣a-z]", " ", text)
    token = tokenizer.morphs(txt)
    token = [t for t in token if t not in STOPWORDS]

    return token

example = text_preprocessing(sentence, mecab)
print("불용어 제거\n" + str(example))