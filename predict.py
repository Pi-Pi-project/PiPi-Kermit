from tensorflow.keras.layers import *
from tensorflow.keras.models import Sequential
from predict_preprocessing import processed_data

input_dim, max_len, X_data = processed_data("a@gmail.com")

model = Sequential()
model.add(Embedding(input_dim+1, 64, mask_zero=True, input_length=max_len))
model.add(Flatten())
model.add(Dense(32, activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.load_weights("weight/model.h5")

model.predict(X_data)