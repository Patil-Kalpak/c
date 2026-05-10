# Ensemble Learning using Boosting
# Algorithm Used : AdaBoost

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# ---------------------------------------------------
# Visualization 2 : Confusion Matrix
# ---------------------------------------------------

 
# ---------------------------------------------------
# Generate Synthetic Dataset
# ---------------------------------------------------

X, y = make_classification(
    n_samples=500,
    n_features=4,
    n_informative=2,
    n_redundant=0,
    random_state=42
)

# Create DataFrame
df = pd.DataFrame(X, columns=[
    'Feature1',
    'Feature2',
    'Feature3',
    'Feature4'
])

df['Target'] = y

print("Dataset:\n")
print(df.head())

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
# AdaBoost Model
# ---------------------------------------------------

model = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=1,
    random_state=42
)

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy :", accuracy)

# ---------------------------------------------------
# Visualization 1 : Dataset
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    X[:,0],
    X[:,1],
    c=y,
    cmap='coolwarm'
)

plt.title("Synthetic Dataset")
plt.xlabel("Feature1")
plt.ylabel("Feature2")

plt.show()

# ---------------------------------------------------
# Visualization 2 : Confusion Matrix
# ---------------------------------------------------

# ---------------------------------------------------
# Visualization 2 : Confusion Matrix
# ---------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

tn, fp, fn, tp = cm.ravel()

print("\nConfusion Matrix:\n")
print(cm)

print("\nTrue Negative (TN) :", tn)
print("False Positive (FP):", fp)
print("False Negative (FN):", fn)
print("True Positive (TP) :", tp)
# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------

print("\nConclusion:")
print("Boosting combines multiple weak learners sequentially.")
print("AdaBoost focuses more on previously misclassified data.")
print("Boosting improves overall prediction accuracy.")