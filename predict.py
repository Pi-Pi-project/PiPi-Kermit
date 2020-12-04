import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"
import numpy as np
from predict_preprocessing import processed_data
from tensorflow.keras.models import load_model

X_data, train_dataset = processed_data("a@gmail.com")

model = load_model("./weight/model.h5")

result = model.predict(X_data)

print(train_dataset.loc[np.argmax(result)])