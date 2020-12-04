import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"
from tensorflow.keras.layers import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from train_preprocessing import processed_data

def model_train(email):
    input_dim, max_len, train_X, train_Y = processed_data(email)

    if not(os.path.isdir("weight")):
        os.makedirs(os.path.join("weight"))

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

    model.save("weight/model.h5")

    # plot_model(history, "RMSprop", False)