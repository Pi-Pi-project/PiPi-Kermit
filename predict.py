import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"
import numpy as np
from tensorflow.keras.models import load_model
from predict_preprocessing import processed_data

def model_predict(email):
    X_data, response_PL = processed_data(email)

    model = load_model("./weight/model.h5")

    result = model.predict(X_data)
    recommand_post = response_PL.loc[np.argmax(result)]

    response_json = {"id": str(recommand_post.id),
                     "title": recommand_post.title,
                     "img": recommand_post.img,
                     "category": recommand_post.cate,
                     "idea": recommand_post.idea,
                     "postSkillsets": [{"postId": str(recommand_post.id), "skill": recommand_post.skillset}],
                     "max": str(recommand_post['max']),
                     "userEmail": recommand_post.email,
                     "userImg": recommand_post.profile_img,
                     "userNickname": recommand_post.nickname,
                     "createdAt": recommand_post.created}

    return response_json