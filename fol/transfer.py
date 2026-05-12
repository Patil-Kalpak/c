# ============================================================
# INSTALL
# ============================================================

# WINDOWS:
# pip install numpy matplotlib tensorflow==2.15.0

# UBUNTU:
# pip3 install numpy matplotlib tensorflow==2.15.0


# ============================================================
# EXP 3 : TRANSFER LEARNING
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.datasets import mnist

# ============================================================
# SYNTHETIC DATASET
# ============================================================

# X_train = np.random.rand(1000,32,32,3)
# X_test = np.random.rand(200,32,32,3)

# y_train = to_categorical(np.random.randint(0,10,1000),10)
# y_test = to_categorical(np.random.randint(0,10,200),10)


# ============================================================
# REAL DATASET (UNCOMMENT)
# ============================================================


# (X_train, y_train), (X_test, y_test) = cifar10.load_data()

# X_train = X_train.astype('float32') / 255
# X_test = X_test.astype('float32') / 255

# y_train = to_categorical(y_train,10)
# y_test = to_categorical(y_test,10)

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

# Convert grayscale to RGB
X_train = np.stack((X_train,)*3, axis=-1)
X_test = np.stack((X_test,)*3, axis=-1)

# Resize to 32x32
import tensorflow as tf

X_train = tf.image.resize(X_train, (32,32))
X_test = tf.image.resize(X_test, (32,32))

y_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)


# ============================================================
# PRETRAINED MODEL
# ============================================================

base_model = MobileNetV2(

    weights='imagenet',
    include_top=False,
    input_shape=(32,32,3)
)


# ============================================================
# MODEL 1 : FROZEN LAYERS
# ============================================================

base_model.trainable = False

model1 = Sequential([

    base_model,

    Flatten(),

    Dense(10, activation='softmax')
])

model1.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\nTRAINING WITH FROZEN LAYERS")

model1.fit(
    X_train,
    y_train,
    epochs=2,
    batch_size=32,
    verbose=0
)

_, acc1 = model1.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"Frozen Layers Accuracy : {acc1:.4f}")


# ============================================================
# MODEL 2 : PARTIAL FINE TUNING
# ============================================================

base_model.trainable = True

# Freeze first few layers only
for layer in base_model.layers[:-20]:

    layer.trainable = False

model2 = Sequential([

    base_model,

    Flatten(),

    Dense(10, activation='softmax')
])

model2.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\nTRAINING WITH PARTIAL FINE TUNING")

model2.fit(
    X_train,
    y_train,
    epochs=2,
    batch_size=32,
    verbose=0
)

_, acc2 = model2.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"Fine Tuned Accuracy : {acc2:.4f}")


# ============================================================
# COMPARISON GRAPH
# ============================================================

models = [
    "Frozen Layers",
    "Fine Tuning"
]

acc = [
    acc1,
    acc2
]

plt.bar(models, acc)

plt.ylabel("Accuracy")

plt.title("Transfer Learning Comparison")

plt.show()


# ============================================================
# OBSERVATIONS
# ============================================================

print("\nOBSERVATIONS:")

print("1. Transfer learning improves performance.")
print("2. Pretrained features help small datasets.")
print("3. Fine tuning may improve accuracy further.")
print("4. Frozen layers train faster.")