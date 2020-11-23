from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import *
from tensorflow.keras.models import Sequential, load_model, Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint,  ReduceLROnPlateau
from tensorflow.keras.regularizers import *
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.optimizers import Adam, RMSprop
import tensorflow as tf
from Preprocessing_Func import get_data, lower, regex, nouns
tf.random.set_seed(777)

# Test Email
email = "a@gmail.com"

tokenizer = Tokenizer()

"""
US: User_Skillset - user_skill
USL: User_Search_Log - search_log
UVL: User_View_Log - id, title, skillset, content, view_log
"""
US, USL, UVL = get_data(email)

US.user_skill = lower(US.user_skill)
USL.search_log = lower(USL.search_log)
UVL.title = nouns(regex(lower(UVL.title)))
UVL.skillset = lower(UVL.skillset)
UVL.content = nouns(regex(lower(UVL.content)))
UVL.view_log = lower(UVL.view_log)

X_train = []
Y_train = []
X_test = []
Y_test = []

tokenizer.fit_on_texts(list(UVL.title))
tokenizer.fit_on_texts(list(UVL.skillset))
tokenizer.fit_on_texts(list(UVL.content))
tokenizer.fit_on_texts(list(USL.search_log))

threshold = 10
total_cnt = len(tokenizer.word_index)
rare_cnt = 0
total_freq = 0
rare_freq = 0

for key, value in tokenizer.word_counts.items():
    total_freq = total_freq + value

    if(value < threshold):
        rare_cnt = rare_cnt + 1
        rare_freq = rare_freq + value

vocab_size = total_cnt - rare_cnt + 1
