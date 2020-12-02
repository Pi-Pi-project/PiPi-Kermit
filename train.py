import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.regularizers import *
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.models import Sequential, load_model, Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from preprocessing import processed_data

# Test Email
email = "a@gmail.com"
input_dim, max_len, train_X, train_Y = processed_data(email)

model = Sequential()
model.add(Embedding(input_dim+1, 64, mask_zero=True, input_length=max_len))
model.add(Flatten())
model.add(Dense(32, activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

from plot_history import plot_model

model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])
history = model.fit(train_X, train_Y, epochs=100, batch_size=64, validation_split=0.1)

model.save_weights("weight/model.h5")

plot_model(history, "RMSprop", False)