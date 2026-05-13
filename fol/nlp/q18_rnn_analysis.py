# Sentiment Analysis using RNN

import nltk
import numpy as np

from nltk.corpus import movie_reviews
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# Download dataset
nltk.download('movie_reviews')

# Load reviews and labels
documents = []

for category in movie_reviews.categories():

    for fileid in movie_reviews.fileids(category):

        review = movie_reviews.raw(fileid)

        documents.append((review, category))

# Separate texts and labels
texts = []
labels = []

for review, category in documents:

    texts.append(review)

    if category == "pos":
        labels.append(1)
    else:
        labels.append(0)

# Tokenization
tokenizer = Tokenizer(num_words=5000)

tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)

# Padding
X = pad_sequences(sequences, maxlen=100)

y = np.array(labels)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Build RNN model
model = Sequential()

model.add(Embedding(input_dim=5000, output_dim=32))

model.add(SimpleRNN(32))

model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(
    X_train,
    y_train,
    epochs=2,
    batch_size=64
)

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)

# Display accuracy
print("\nAccuracy =", round(accuracy * 100, 2), "%")