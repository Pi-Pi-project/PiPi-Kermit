from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer()

samples = ["The cat sat on the mat.", "The dog ate my homework"]

tokenizer.fit_on_texts(samples)

sequences = tokenizer.texts_to_sequences(samples)

# Mode: binary, count, tfidf, freq
one_hot_result = tokenizer.texts_to_matrix(samples, mode="binary")

word_index = tokenizer.word_index
print("Found %s unique tokens" % len(word_index))

print("Sequence: %s" % sequences)
print("One hot result: ", one_hot_result)