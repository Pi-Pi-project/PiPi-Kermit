from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from DB_preprocessing import processed_data
from DB_get_data import _user_view_log

email = "a@gmail.com"

SL, SLL, VTL, VCL, VLL = processed_data(email)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(VCL)

encoded = tokenizer.texts_to_sequences(VCL)
max_len = max(len(l) for l in encoded)

x_train = pad_sequences(encoded, maxlen=max_len, padding="post")
print(encoded)
print(x_train)