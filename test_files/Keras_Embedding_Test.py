from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from DB_preprocessing import processed_data
import numpy as np

email = "a@gmail.com"
SL, SLL, VTL, VCL, VLL = processed_data(email)

# y_train = [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0]
y_train = [1, 1, 0, 1, 0]

tokenizer = Tokenizer()

def embedding(input_data, label):
    dataset = []
    for data in input_data:
        tokenizer.fit_on_texts(data)
        dataset.extend(data)

    # print(dataset)
    print("Length of dataset:", len(dataset))
    encoded = tokenizer.texts_to_sequences(dataset)
    print(encoded)
    print("Length of encoded: ", len(encoded))
    vocab_size = len(tokenizer.word_index) + 1
    max_len = max(len(length) for length in encoded)

    # X = pad_sequences(encoded, padding="post")
    X = pad_sequences(encoded, maxlen=max_len, padding="post")
    Y = np.array(label)

    return X, Y, vocab_size, max_len

X, Y, vocab_size, max_len = embedding([SL, SLL, VTL, VCL, VLL], y_train)

print(X.shape)
print(Y.shape)
print(vocab_size)

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Embedding, Flatten
#
# model = Sequential()
# model.add(Embedding(vocab_size, 5, input_length=max_len))
# model.add(Flatten())
# model.add(Dense(1, activation="sigmoid"))
#
# model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["acc"])
# model.fit(X, Y, epochs=100, verbose=2)