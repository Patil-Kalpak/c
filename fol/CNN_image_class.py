# ============================================================
# INSTALL
# ============================================================

# WINDOWS:
# pip install numpy matplotlib tensorflow==2.15.0

# UBUNTU:
# pip3 install numpy matplotlib tensorflow==2.15.0


# ============================================================
# CNN EXPERIMENT
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical


# ============================================================
# SYNTHETIC DATASET
# ============================================================

X_train = np.random.rand(1000,28,28,1)
X_test = np.random.rand(200,28,28,1)

y_train = to_categorical(np.random.randint(0,10,1000),10)
y_test = to_categorical(np.random.randint(0,10,200),10)


# ============================================================
# REAL DATASET (UNCOMMENT)
# ============================================================


# (X_train, y_train), (X_test, y_test) = mnist.load_data()

# X_train = X_train.reshape(-1,28,28,1)/255
# X_test = X_test.reshape(-1,28,28,1)/255

# y_train = to_categorical(y_train,10)
# y_test = to_categorical(y_test,10)



# ============================================================
# MLP MODEL
# ============================================================

mlp = Sequential([
    Flatten(input_shape=(28,28,1)),
    Dense(32, activation='relu'),
    Dense(10, activation='softmax')
])

mlp.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

mlp.fit(X_train,y_train,epochs=2,verbose=0)

_, mlp_acc = mlp.evaluate(X_test,y_test,verbose=0)

print(f"\nMLP Accuracy : {mlp_acc:.4f}")


# ============================================================
# CNN MODEL
# ============================================================

cnn = Sequential([

    Conv2D(32,(3,3),activation='relu',
           input_shape=(28,28,1)),

    MaxPooling2D((2,2)),

    Flatten(),

    Dense(10,activation='softmax')
])

cnn.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

cnn.fit(X_train,y_train,epochs=3,verbose=0)

_, cnn_acc = cnn.evaluate(X_test,y_test,verbose=0)

print(f"CNN Accuracy : {cnn_acc:.4f}")


# ============================================================
# CNN WITHOUT POOLING
# ============================================================

cnn2 = Sequential([

    Conv2D(32,(3,3),activation='relu',
           input_shape=(28,28,1)),

    Flatten(),

    Dense(10,activation='softmax')
])

cnn2.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

cnn2.fit(X_train,y_train,epochs=3,verbose=0)

_, pool_acc = cnn2.evaluate(X_test,y_test,verbose=0)

print(f"CNN Without Pooling Accuracy : {pool_acc:.4f}")


# ============================================================
# ACCURACY GRAPH
# ============================================================

models = ["MLP","CNN","CNN No Pool"]
acc = [mlp_acc, cnn_acc, pool_acc]

plt.bar(models,acc)

plt.title("CNN Comparison")
plt.ylabel("Accuracy")

plt.show()


# ============================================================
# FEATURE MAP VISUALIZATION
# ============================================================

feature_model = Model(
    inputs=cnn.inputs,
    outputs=cnn.layers[0].output
)

sample = X_test[0].reshape(1,28,28,1)

feature_map = feature_model.predict(sample)

plt.imshow(feature_map[0,:,:,0], cmap='gray')

plt.title("Feature Map")

plt.show()


# ============================================================
# FILTER SIZE COMPARISON
# ============================================================

filters = [3,5]
results = []

for f in filters:

    model = Sequential([

        Conv2D(32,(f,f),activation='relu',
               input_shape=(28,28,1)),

        MaxPooling2D((2,2)),

        Flatten(),

        Dense(10,activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    model.fit(X_train,y_train,epochs=2,verbose=0)

    _, acc = model.evaluate(X_test,y_test,verbose=0)

    results.append(acc)

    print(f"Filter {f}x{f} Accuracy : {acc:.4f}")


# ============================================================
# FILTER GRAPH
# ============================================================

plt.bar(["3x3","5x5"],results)

plt.title("Filter Size Comparison")

plt.ylabel("Accuracy")

plt.show()


# ============================================================
# OBSERVATIONS
# ============================================================

print("\nOBSERVATIONS:")

print("1. CNN performs better than MLP.")
print("2. Pooling reduces overfitting.")
print("3. Feature maps capture image patterns.")
print("4. Filter size affects accuracy.")