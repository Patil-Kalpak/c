# EXP 8 : LSTM for Next Word Prediction

# Install once before running:
# py -3.11 -m pip install tensorflow numpy scikit-learn

# ---------------------------------------------------
# Import Libraries
# ---------------------------------------------------

import numpy as np

from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM
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

# text = """
# deep learning is powerful and useful
# machine learning improves prediction accuracy
# artificial intelligence is growing rapidly
# lstm networks remember long term dependencies
# recurrent neural networks process sequential data
# deep learning models are widely used in healthcare
# """

# ---------------- DATASET TEXT ----------------

# Uncomment below if using dataset text file

with open("sample.txt", "r") as file:
    text = file.read()

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

rnn_model = Sequential()

rnn_model.add(
    Embedding(
        input_dim=total_words,
        output_dim=10
    )
)

rnn_model.add(
    SimpleRNN(50)
)

rnn_model.add(
    Dense(total_words, activation='softmax')
)

# ---------------------------------------------------
# Compile Simple RNN
# ---------------------------------------------------

rnn_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# ---------------------------------------------------
# Train Simple RNN
# ---------------------------------------------------

rnn_model.fit(
    X_train,
    y_train,
    epochs=50,
    verbose=0
)

# ---------------------------------------------------
# Evaluate Simple RNN
# ---------------------------------------------------

rnn_loss, rnn_accuracy = rnn_model.evaluate(
    X_test,
    y_test,
    verbose=0
)

# ---------------------------------------------------
# Build LSTM Model
# ---------------------------------------------------

lstm_model = Sequential()

lstm_model.add(
    Embedding(
        input_dim=total_words,
        output_dim=10
    )
)

lstm_model.add(
    LSTM(50)
)

lstm_model.add(
    Dense(total_words, activation='softmax')
)

# ---------------------------------------------------
# Compile LSTM
# ---------------------------------------------------

lstm_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# ---------------------------------------------------
# Train LSTM
# ---------------------------------------------------

lstm_model.fit(
    X_train,
    y_train,
    epochs=50,
    verbose=0
)

# ---------------------------------------------------
# Evaluate LSTM
# ---------------------------------------------------

lstm_loss, lstm_accuracy = lstm_model.evaluate(
    X_test,
    y_test,
    verbose=0
)

# ---------------------------------------------------
# Print Performance Comparison
# ---------------------------------------------------

print("\nSimple RNN Performance")

print("Testing Loss :", round(rnn_loss, 4))

print("Testing Accuracy :", round(rnn_accuracy, 4))

print("\nLSTM Performance")

print("Testing Loss :", round(lstm_loss, 4))

print("Testing Accuracy :", round(lstm_accuracy, 4))

# ---------------------------------------------------
# Next Word Prediction using LSTM
# ---------------------------------------------------

input_text = "deep learning"

# Convert into sequence
token_text = tokenizer.texts_to_sequences([input_text])[0]

# Padding
token_text = pad_sequences(
    [token_text],
    maxlen=max_sequence_len - 1,
    padding='pre'
)

# Predict next word
predicted = lstm_model.predict(
    token_text,
    verbose=0
)

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

print("1. LSTM handles long-term dependencies better than Simple RNN.")

print("2. LSTM generally achieves lower loss and better prediction accuracy.")

print("3. Memory cells in LSTM help retain important sequence information.")

print("4. Simple RNN struggles because of vanishing gradient problem.")

print("5. LSTM improves sequence learning and prediction quality.")