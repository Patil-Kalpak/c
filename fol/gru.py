import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN,LSTM,GRU,Dense
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# ---------------- DATASET TEXT ----------------
if os.path.exists("sample.txt"):
    with open("text_data.txt","r") as f:
        text=f.read().lower()

# ---------------- SYNTHETIC TEXT ----------------
else:
    print("text_data.txt not found! Using fallback text...")
    text="""
    deep learning is powerful and useful
    machine learning improves prediction accuracy
    recurrent neural networks process sequential data
    lstm handles long term dependencies
    gru trains faster than lstm
    artificial intelligence is growing rapidly
    """*20

# Character Mapping
chars=sorted(list(set(text)))
char_to_int={c:i for i,c in enumerate(chars)}
n_vocab=len(chars)

# Create Sequences
seq_length=10
X_data=[]
y_data=[]

for i in range(len(text)-seq_length):
    seq_in=text[i:i+seq_length]
    seq_out=text[i+seq_length]
    X_data.append([char_to_int[char] for char in seq_in])
    y_data.append(char_to_int[seq_out])

# Reshape and Normalize
X=np.reshape(X_data,(len(X_data),seq_length,1))
X=X/float(n_vocab)

# One Hot Encoding
y=tf.keras.utils.to_categorical(y_data)

# Train Test Split
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

print(f"\nVocabulary Size : {n_vocab}")
print(f"Total Sequences : {len(X_data)}")

# Model Training
histories={}

for model_name,LayerType in [
    ("RNN",SimpleRNN),
    ("LSTM",LSTM),
    ("GRU",GRU)
]:

    print(f"\nTraining {model_name} Model...")

    model=Sequential([
        LayerType(128,input_shape=(seq_length,1)),
        Dense(n_vocab,activation='softmax')
    ])

    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    history=model.fit(
        X_train,
        y_train,
        epochs=10,
        batch_size=64,
        validation_data=(X_test,y_test),
        verbose=0
    )

    histories[model_name]=history

# Print Final Results
for name,h in histories.items():

    print(f"\n{name} Final Results")

    print(
        "Training Accuracy :",
        round(h.history['accuracy'][-1],4)
    )

    print(
        "Testing Accuracy :",
        round(h.history['val_accuracy'][-1],4)
    )

    print(
        "Training Loss :",
        round(h.history['loss'][-1],4)
    )

    print(
        "Testing Loss :",
        round(h.history['val_loss'][-1],4)
    )

# Plot Accuracy Graph
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)

for name,h in histories.items():
    plt.plot(h.history['accuracy'],label=f'{name} Train')
    plt.plot(h.history['val_accuracy'],linestyle='--',label=f'{name} Test')

plt.title("Training vs Testing Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()

# Plot Loss Graph
plt.subplot(1,2,2)

for name,h in histories.items():
    plt.plot(h.history['loss'],label=f'{name} Train')
    plt.plot(h.history['val_loss'],linestyle='--',label=f'{name} Test')

plt.title("Training vs Testing Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()

# Save Graph
plt.tight_layout()
plt.savefig("Exp7_8_9_Comparison.png")
plt.close()

print("\nComparison plot saved as: Exp7_8_9_Comparison.png")
print("Experiments 7, 8, and 9 Completed!")