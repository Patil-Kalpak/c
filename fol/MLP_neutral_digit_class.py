# ============================================================
# INSTALL REQUIRED LIBRARIES
# ============================================================

# WINDOWS:
# pip install numpy matplotlib scikit-learn tensorflow==2.15.0

# UBUNTU:
# pip3 install numpy matplotlib scikit-learn tensorflow==2.15.0


# ============================================================
# EXP 1 : MLP (Multilayer Perceptron)
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist


# ============================================================
# SYNTHETIC DATASET (ACTIVE)
# ============================================================

X, y = make_classification(
    n_samples=3000,
    n_features=64,
    n_informative=50,
    n_classes=10,
    random_state=42
)

# Normalize
scaler = StandardScaler()
X = scaler.fit_transform(X)

# One-hot encoding
y = to_categorical(y, 10)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ============================================================
# REAL DATASET (UNCOMMENT DURING FINAL RUN)
# ============================================================


# (X_train, y_train), (X_test, y_test) = mnist.load_data()

# X_train = X_train.reshape(60000, 784).astype('float32') / 255
# X_test = X_test.reshape(10000, 784).astype('float32') / 255

# y_train = to_categorical(y_train, 10)
# y_test = to_categorical(y_test, 10)



# ============================================================
# FUNCTION TO CREATE MODEL
# ============================================================

def create_model(hidden_layers, activation_function):

    model = Sequential()

    # First hidden layer
    model.add(
        Dense(
            hidden_layers[0],
            activation=activation_function,
            input_shape=(X_train.shape[1],)
        )
    )

    # Remaining hidden layers
    for neurons in hidden_layers[1:]:

        model.add(
            Dense(
                neurons,
                activation=activation_function
            )
        )

    # Output layer
    model.add(Dense(10, activation='softmax'))

    # Compile model
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


# ============================================================
# SETTINGS
# ============================================================

activation_functions = ['relu', 'sigmoid', 'tanh']

hidden_layer_configs = [
    [64],
    [128, 64],
    [256, 128, 64]
]

results = []

labels = []
accuracies = []


# ============================================================
# TRAINING
# ============================================================

for activation in activation_functions:

    for layers in hidden_layer_configs:

        print("\n================================================")
        print(f"Activation Function : {activation}")
        print(f"Hidden Layers       : {layers}")
        print("================================================")

        # Create model
        model = create_model(layers, activation)

        # Train model
        history = model.fit(
            X_train,
            y_train,
            epochs=5,
            batch_size=32,
            validation_split=0.2,
            verbose=0
        )

        # Evaluate model
        loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

        # Final train + validation accuracy
        train_acc = history.history['accuracy'][-1]
        val_acc = history.history['val_accuracy'][-1]

        # Print results
        print(f"Training Accuracy   : {train_acc:.4f}")
        print(f"Validation Accuracy : {val_acc:.4f}")
        print(f"Test Accuracy       : {accuracy:.4f}")
        print(f"Loss                : {loss:.4f}")

        # Store results
        results.append({
            'activation': activation,
            'layers': str(layers),
            'accuracy': accuracy
        })

        labels.append(f"{activation}\n{layers}")
        accuracies.append(accuracy)


# ============================================================
# FINAL COMPARISON GRAPH
# ============================================================

plt.figure(figsize=(12,5))

plt.bar(labels, accuracies)

plt.xlabel("Activation Function and Hidden Layers")
plt.ylabel("Accuracy")
plt.title("MLP Performance Comparison")

plt.xticks(rotation=15)

plt.grid(True)

plt.show()


# ============================================================
# FINAL RESULTS
# ============================================================

print("\n\n================ FINAL RESULTS ================\n")

for r in results:

    print(f"Activation : {r['activation']}")
    print(f"Layers     : {r['layers']}")
    print(f"Accuracy   : {r['accuracy']:.4f}")

    print("------------------------------------------------")


# ============================================================
# OBSERVATIONS
# ============================================================

print("\n================ OBSERVATIONS ================\n")

print("1. ReLU converges faster than sigmoid.")
print("2. Sigmoid gives lower accuracy because of vanishing gradients.")
print("3. Tanh performs better than sigmoid in many cases.")
print("4. Increasing hidden layers improves learning capacity.")
print("5. Very deep networks may lead to overfitting.")
print("6. Validation accuracy helps measure generalization.")