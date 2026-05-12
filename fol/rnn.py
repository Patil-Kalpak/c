# EXP 7 : Simple RNN for Next Word Prediction

# Install once before running:
# py -3.11 -m pip install tensorflow numpy scikit-learn

# ---------------------------------------------------
# Import Libraries
# ---------------------------------------------------

import numpy as np

from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Embedding

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

# ---------------------------------------------------
# TEXT DATA
# ---------------------------------------------------

# ---------------- SYNTHETIC TEXT ----------------

text = """
deep learning is powerful
deep learning is interesting
machine learning is useful
artificial intelligence is growing
deep learning helps in prediction
"""

# ---------------- DATASET TEXT ----------------

# Uncomment below if using dataset text file

# with open("sample.txt", "r") as file:
#     text = file.read()

# ---------------------------------------------------
# Tokenization
# ---------------------------------------------------

tokenizer = Tokenizer()

tokenizer.fit_on_texts([text])

total_words = len(tokenizer.word_index) + 1

# Convert text into sequence
token_list = tokenizer.texts_to_sequences([text])[0]

# ---------------------------------------------------
# Create Input Sequences
# ---------------------------------------------------

input_sequences = []

for i in range(1, len(token_list)):

    sequence = token_list[:i + 1]

    input_sequences.append(sequence)

# ---------------------------------------------------
# Padding
# ---------------------------------------------------

max_sequence_len = max([len(seq) for seq in input_sequences])

input_sequences = pad_sequences(
    input_sequences,
    maxlen=max_sequence_len,
    padding='pre'
)

# ---------------------------------------------------
# Split into X and y
# ---------------------------------------------------

X = input_sequences[:, :-1]

y = input_sequences[:, -1]

# One-hot encoding
y = to_categorical(y, num_classes=total_words)

# ---------------------------------------------------
# Train Test Split
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------------------
# Build Simple RNN Model
# ---------------------------------------------------

model = Sequential()

# Embedding Layer
model.add(
    Embedding(
        input_dim=total_words,
        output_dim=10,
        input_length=max_sequence_len - 1
    )
)

# Simple RNN Layer
model.add(
    SimpleRNN(50)
)

# Output Layer
model.add(
    Dense(total_words, activation='softmax')
)

# ---------------------------------------------------
# Compile Model
# ---------------------------------------------------

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# ---------------------------------------------------
# Train Model
# ---------------------------------------------------

model.fit(
    X_train,
    y_train,
    epochs=50,
    verbose=1
)

# ---------------------------------------------------
# Training Performance
# ---------------------------------------------------

train_loss, train_accuracy = model.evaluate(
    X_train,
    y_train,
    verbose=0
)

print("\nTraining Loss :", round(train_loss, 4))

print("Training Accuracy :", round(train_accuracy, 4))

# ---------------------------------------------------
# Testing Performance
# ---------------------------------------------------

test_loss, test_accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("\nTesting Loss :", round(test_loss, 4))

print("Testing Accuracy :", round(test_accuracy, 4))

# ---------------------------------------------------
# Next Word Prediction
# ---------------------------------------------------

input_text = "deep learning"

# Convert text into sequence
token_text = tokenizer.texts_to_sequences([input_text])[0]

# Padding
token_text = pad_sequences(
    [token_text],
    maxlen=max_sequence_len - 1,
    padding='pre'
)

# Predict next word
predicted = model.predict(token_text, verbose=0)

predicted_word_index = np.argmax(predicted)

# Find predicted word
for word, index in tokenizer.word_index.items():

    if index == predicted_word_index:

        predicted_word = word
        break

print("\nInput Text :", input_text)

print("Predicted Next Word :", predicted_word)

# ---------------------------------------------------
# Analysis
# ---------------------------------------------------

print("\nAnalysis:")

print("1. Simple RNN predicts the next word using previous sequence information.")

print("2. Short sequences generally provide better prediction accuracy.")

print("3. Long sequences are difficult for Simple RNN because of vanishing gradient problem.")

print("4. Basic RNN cannot effectively remember long-term dependencies.")

print("5. Training accuracy is usually higher than testing accuracy.")