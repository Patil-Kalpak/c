# EXP 10 : Linear Discriminant Analysis (LDA)

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# ---------------------------------------------------
# Load Digits Dataset
# ---------------------------------------------------

digits = load_digits()

X = digits.data
y = digits.target

print("Dataset Shape :", X.shape)

# ---------------------------------------------------
# Visualization 1 : Sample Image
# ---------------------------------------------------

plt.figure(figsize=(4,4))

plt.imshow(
    digits.images[0],
    cmap='gray'
)

plt.title(f"Digit : {y[0]}")

plt.show()

# ---------------------------------------------------
# Split Dataset
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------------------
# KNN Before LDA
# ---------------------------------------------------

knn_before = KNeighborsClassifier()

knn_before.fit(X_train, y_train)

y_pred_before = knn_before.predict(X_test)

acc_before = accuracy_score(
    y_test,
    y_pred_before
)

print("\nAccuracy Before LDA :", acc_before)

# ---------------------------------------------------
# Apply LDA
# ---------------------------------------------------

lda = LinearDiscriminantAnalysis(
    n_components=6
)

X_train_lda = lda.fit_transform(
    X_train,
    y_train
)

X_test_lda = lda.transform(X_test)

print("\nShape After LDA :", X_train_lda.shape)

# ---------------------------------------------------
# Visualization 2 : LDA Reduced Data
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    X_train_lda[:,0],
    X_train_lda[:,1],
    c=y_train,
    cmap='viridis'
)

plt.title("LDA Visualization")
plt.xlabel("LD1")
plt.ylabel("LD2")

plt.show()

# ---------------------------------------------------
# KNN After LDA
# ---------------------------------------------------

knn_after = KNeighborsClassifier()

knn_after.fit(
    X_train_lda,
    y_train
)

y_pred_after = knn_after.predict(X_test_lda)

acc_after = accuracy_score(
    y_test,
    y_pred_after
)

print("\nAccuracy After LDA :", acc_after)

# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------

print("\nConclusion:")
print("LDA reduces dimensions while preserving class separation.")
print("The dataset was reduced from 64 dimensions to 6 dimensions.")
print("Some classification accuracy decreased due to information loss.")