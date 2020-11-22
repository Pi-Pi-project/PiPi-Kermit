# Recommendation System Developing 👨‍💻

Source/Reference: [당근마켓 - 딥러닝 개인화 추천](https://medium.com/daangn/%EB%94%A5%EB%9F%AC%EB%8B%9D-%EA%B0%9C%EC%9D%B8%ED%99%94-%EC%B6%94%EC%B2%9C-1eda682c2e8c), [Matrix Factorization for CF](https://ogrisel.github.io/decks/2017_dotai_neural_recsys/#17), [Deep Neural Networks for YouTube Recommendations](https://static.googleusercontent.com/media/research.google.com/ko//pubs/archive/45530.pdf)

## Symbolic Variables

- Recommender Systems
  - post_id
  - user_email
- Categorical Descriptors
  - user_skill
  - search_log
  - post_title
  - post_content
  - view_log

## Models

### compile option

- optimizer=RMSprop
- loss=categorical_crossentropy
- callback=RediceLROnPlateau, EarlyStopping, ModelCheckpoint

### Model1

- Embedding
- Conv1D - relu, padding=same
- GlobalMaxPooling1D
- Dense - softmax

### Model2

- Embedding
- Conv1D - relu
- MaxPooling
- Dropout
- Conv1D - relu
- GlobalMaxPooling1D
- BatchNormalization
- Dense - softmax

### Model3

- Embedding
- Conv1D - relu
- Conv1D - relu
- Conv1D - relu
- MaxPooling1D
- LSTM
- Dropout
- Dense - softmax

### Model4

- Embedding
- Dropout
- Conv1D - relu
- MaxPooling
- LSTM
- Dense - softmax