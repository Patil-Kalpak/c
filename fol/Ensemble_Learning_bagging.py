# Ensemble Learning using Bagging
# Algorithm Used : Random Forest

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

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

print(df.head())

# ---------------------------------------------------
# Split Dataset
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------------------
# Random Forest Model
# ---------------------------------------------------

model = RandomForestClassifier(
    n_estimators=50,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy :", accuracy)

# ---------------------------------------------------
# Visualization
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    X[:,0],
    X[:,1],
    c=y,
)

plt.title("Synthetic Dataset")
plt.xlabel("Feature1")
plt.ylabel("Feature2")

plt.show()


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
print("Bagging combines multiple models trained independently.")
print("Random Forest is a popular bagging algorithm.")
print("It improves accuracy and reduces overfitting.")