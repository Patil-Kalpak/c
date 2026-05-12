# ============================================================
# INSTALL
# ============================================================

# WINDOWS:
# pip install numpy matplotlib tensorflow==2.15.0

# UBUNTU:
# pip3 install numpy matplotlib tensorflow==2.15.0


# ============================================================
# EXP 4 : CNN vs TRANSFER LEARNING
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
import time
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.utils import to_categorical

from tensorflow.keras.datasets import mnist


# ============================================================
# SYNTHETIC DATASET
# ============================================================

# X_train = np.random.rand(300,32,32,3)
# X_test = np.random.rand(60,32,32,3)

# y_train = to_categorical(np.random.randint(0,10,300),10)
# y_test = to_categorical(np.random.randint(0,10,60),10)


# ============================================================
# REAL DATASET
# ============================================================

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

# Convert grayscale to RGB
X_train = np.stack((X_train,)*3, axis=-1)
X_test = np.stack((X_test,)*3, axis=-1)

# Resize to 32x32
X_train = tf.image.resize(X_train, (32,32))
X_test = tf.image.resize(X_test, (32,32))

y_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)


# ============================================================
# MODEL 1 : CNN FROM SCRATCH
# ============================================================

cnn = Sequential([

    Conv2D(16,(3,3),activation='relu',
           input_shape=(32,32,3)),

    MaxPooling2D((2,2)),

    Flatten(),

    Dense(10,activation='softmax')
])

cnn.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\nTRAINING CNN FROM SCRATCH")

start = time.time()

cnn.fit(
    X_train,
    y_train,
    epochs=2,
    batch_size=32,
    verbose=0
)

cnn_time = time.time() - start

_, cnn_acc = cnn.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"CNN Accuracy      : {cnn_acc:.4f}")
print(f"Training Time     : {cnn_time:.2f} sec")


# ============================================================
# MODEL 2 : TRANSFER LEARNING
# ============================================================

base_model = MobileNetV2(

    weights='imagenet',
    include_top=False,
    input_shape=(32,32,3)
)

base_model.trainable = False

transfer_model = Sequential([

    base_model,

    Flatten(),

    Dense(10,activation='softmax')
])

transfer_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\nTRAINING TRANSFER LEARNING MODEL")

start = time.time()

transfer_model.fit(
    X_train,
    y_train,
    epochs=2,
    batch_size=32,
    verbose=0
)

transfer_time = time.time() - start

_, transfer_acc = transfer_model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"Transfer Accuracy : {transfer_acc:.4f}")
print(f"Training Time     : {transfer_time:.2f} sec")


# ============================================================
# ACCURACY GRAPH
# ============================================================

models = ["CNN","Transfer Learning"]

acc = [cnn_acc, transfer_acc]

plt.bar(models, acc)

plt.ylabel("Accuracy")

plt.title("CNN vs Transfer Learning")

plt.show()


# ============================================================
# TRAINING TIME GRAPH
# ============================================================

times = [cnn_time, transfer_time]

plt.bar(models, times)

plt.ylabel("Seconds")

plt.title("Training Time Comparison")

plt.show()


# ============================================================
# OBSERVATIONS
# ============================================================

print("\nOBSERVATIONS:")

print("1. Transfer learning uses pretrained features.")
print("2. CNN learns completely from scratch.")
print("3. Transfer learning usually gives better accuracy.")
print("4. Transfer learning is useful for small datasets.")
print("5. CNN training may take longer for complex datasets.")