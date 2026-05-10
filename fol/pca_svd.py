# EXP 9 : PCA and SVD using Synthetic Dataset

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD

# ---------------------------------------------------
# Generate Synthetic Dataset
# ---------------------------------------------------

X, y = make_classification(
    n_samples=300,
    n_features=6,
    n_informative=4,
    n_redundant=0,
    random_state=42
)

# Create DataFrame
df = pd.DataFrame(
    X,
    columns=[
        'Feature1',
        'Feature2',
        'Feature3',
        'Feature4',
        'Feature5',
        'Feature6'
    ]
)

# Add Target Column
df['Target'] = y

print("Original Dataset:\n")
print(df.head())

print("\nOriginal Shape :", X.shape)

# ---------------------------------------------------
# Apply PCA
# ---------------------------------------------------

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

print("\nShape After PCA :", X_pca.shape)

print("\nPCA Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

# ---------------------------------------------------
# Visualization 1 : PCA
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c=y,
    cmap='viridis'
)

plt.title("PCA Visualization")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.show()

# ---------------------------------------------------
# Apply SVD
# ---------------------------------------------------

svd = TruncatedSVD(n_components=2)

X_svd = svd.fit_transform(X)

print("\nShape After SVD :", X_svd.shape)

print("\nSVD Explained Variance Ratio:")
print(svd.explained_variance_ratio_)

# ---------------------------------------------------
# Visualization 3 : PCA Variance Contribution
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.bar(
    range(1, len(pca.explained_variance_ratio_) + 1),
    pca.explained_variance_ratio_
)

plt.title("PCA Variance Contribution")
plt.xlabel("Principal Components")
plt.ylabel("Explained Variance Ratio")

plt.show()

# ---------------------------------------------------
# Visualization 2 : SVD
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    X_svd[:,0],
    X_svd[:,1],
    c=y,
    cmap='plasma'
)

plt.title("SVD Visualization")
plt.xlabel("Component 1")
plt.ylabel("Component 2")

plt.show()



# ---------------------------------------------------
# Visualization 4 : SVD Variance Contribution
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.bar(
    range(1, len(svd.explained_variance_ratio_) + 1),
    svd.explained_variance_ratio_
)

plt.title("SVD Variance Contribution")
plt.xlabel("Components")
plt.ylabel("Explained Variance Ratio")

plt.show()
# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------

print("\nConclusion:")
print("PCA and SVD are dimensionality reduction techniques.")
print("Both reduce the number of features while preserving information.")
print("The dataset was reduced from 6 dimensions to 2 dimensions.")