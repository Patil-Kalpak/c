# ============================================================
# INSTALL
# ============================================================

# WINDOWS:
# pip install numpy matplotlib tensorflow==2.15.0

# UBUNTU:
# pip3 install numpy matplotlib tensorflow==2.15.0


# ============================================================
# EXP 5 : PERFORMANCE ANALYSIS OF CNN
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense

from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

from tensorflow.keras.datasets import mnist


# ============================================================
# SYNTHETIC DATASET
# ============================================================

# X_train = np.random.rand(300,28,28,1)
# X_test = np.random.rand(60,28,28,1)

# y_train = to_categorical(np.random.randint(0,10,300),10)
# y_test = to_categorical(np.random.randint(0,10,60),10)


# ============================================================
# REAL DATASET
# ============================================================

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(-1,28,28,1) / 255
X_test = X_test.reshape(-1,28,28,1) / 255

y_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)


# ============================================================
# FUNCTION TO CREATE CNN
# ============================================================

def create_model(lr):

    model = Sequential([

        Conv2D(
            16,
            (3,3),
            activation='relu',
            input_shape=(28,28,1)
        ),

        MaxPooling2D((2,2)),

        Flatten(),

        Dense(10,activation='softmax')
    ])

    model.compile(
        optimizer=Adam(learning_rate=lr),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


# ============================================================
# LEARNING RATE ANALYSIS
# ============================================================

learning_rates = [0.1, 0.01, 0.001]

lr_results = []

for lr in learning_rates:

    print(f"\nTRAINING WITH LEARNING RATE = {lr}")

    model = create_model(lr)

    model.fit(

        X_train,
        y_train,

        epochs=5,
        validation_split=0.2,

        batch_size=32,
        verbose=0
    )

    _, acc = model.evaluate(
        X_test,
        y_test,
        verbose=0
    )

    lr_results.append(acc)

    print(f"Accuracy : {acc:.4f}")


# ============================================================
# LEARNING RATE GRAPH
# ============================================================

plt.bar(
    ["0.1","0.01","0.001"],
    lr_results
)

plt.title("Learning Rate Comparison")

plt.ylabel("Accuracy")

plt.show()


# ============================================================
# EPOCH ANALYSIS
# ============================================================

epochs_list = [3,5,10]

epoch_results = []

for e in epochs_list:

    print(f"\nTRAINING WITH EPOCHS = {e}")

    model = create_model(0.001)

    history = model.fit(

        X_train,
        y_train,

        epochs=e,
        validation_split=0.2,

        batch_size=32,
        verbose=0
    )

    _, acc = model.evaluate(
        X_test,
        y_test,
        verbose=0
    )

    epoch_results.append(acc)

    print(f"Accuracy : {acc:.4f}")


# ============================================================
# EPOCH GRAPH
# ============================================================

plt.bar(
    ["3","5","10"],
    epoch_results
)

plt.title("Epoch Comparison")

plt.ylabel("Accuracy")

plt.xlabel("Epochs")

plt.show()


# ============================================================
# LOSS CURVE
# ============================================================

plt.plot(history.history['loss'])

plt.plot(history.history['val_loss'])

plt.legend([
    "Training Loss",
    "Validation Loss"
])

plt.title("Loss Curve")

plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.show()


# ============================================================
# ACCURACY CURVE
# ============================================================

plt.plot(history.history['accuracy'])

plt.plot(history.history['val_accuracy'])

plt.legend([
    "Training Accuracy",
    "Validation Accuracy"
])

plt.title("Accuracy Curve")

plt.xlabel("Epochs")
plt.ylabel("Accuracy")

plt.show()


# ============================================================
# FINAL ACCURACY
# ============================================================

_, final_acc = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(f"\nFinal Accuracy : {final_acc:.4f}")


# ============================================================
# OBSERVATIONS
# ============================================================

print("\nOBSERVATIONS:")

print("1. Learning rate affects convergence speed.")
print("2. Very high learning rate may cause instability.")
print("3. Increasing epochs improves learning initially.")
print("4. Too many epochs may lead to overfitting.")
print("5. Validation loss helps detect generalization.")