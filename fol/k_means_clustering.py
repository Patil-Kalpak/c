# EXP 7 : K-Means Clustering with More Noise

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# ---------------------------------------------------
# Generate Synthetic Dataset
# ---------------------------------------------------

X, y = make_blobs(
    n_samples=300,
    centers=3,
    cluster_std=2.5,   # Increased spread
    n_features=2,
    random_state=42
)

# Create DataFrame
df = pd.DataFrame(
    X,
    columns=['Feature1', 'Feature2']
)

print("Original Dataset:\n")
print(df.head())

# ---------------------------------------------------
# Visualization 1 : Original Dataset
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    X[:,0],
    X[:,1]
)

plt.title("Original Dataset")
plt.xlabel("Feature1")
plt.ylabel("Feature2")

plt.show()

# ---------------------------------------------------
# Add More Random Noise
# ---------------------------------------------------

noise = np.random.normal(
    0,
    3,          # Increased noise
    X.shape
)

X_noisy = X + noise

# Noisy Dataset
df_noisy = pd.DataFrame(
    X_noisy,
    columns=['Feature1', 'Feature2']
)

print("\nDataset After Adding Noise:\n")
print(df_noisy.head())

# ---------------------------------------------------
# Visualization 2 : Noisy Dataset
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    X_noisy[:,0],
    X_noisy[:,1]
)

plt.title("Dataset After Adding Noise")
plt.xlabel("Feature1")
plt.ylabel("Feature2")

plt.show()

# ---------------------------------------------------
# Apply K-Means Clustering
# ---------------------------------------------------

kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

kmeans.fit(X_noisy)

# Predicted Clusters
clusters = kmeans.predict(X_noisy)

# Cluster Centers
centroids = kmeans.cluster_centers_

print("\nCluster Centers:\n")
print(centroids)

# ---------------------------------------------------
# Visualization 3 : K-Means Clustering
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    X_noisy[:,0],
    X_noisy[:,1],
    c=clusters,
    cmap='viridis'
)

# Plot Centroids
plt.scatter(
    centroids[:,0],
    centroids[:,1],
    s=250,
    marker='X'
)

plt.title("K-Means Clustering on Noisy Data")
plt.xlabel("Feature1")
plt.ylabel("Feature2")

plt.show()

# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------

# ---------------------------------------------------
# Cluster Information
# ---------------------------------------------------

print("\nNumber of Clusters :", kmeans.n_clusters)

# Count points in each cluster
unique, counts = np.unique(clusters, return_counts=True)

print("\nPoints in Each Cluster:")

for i in range(len(unique)):
    print("Cluster", unique[i], ":", counts[i], "points")

# Inertia / WCSS
print("\nWCSS (Inertia) :", kmeans.inertia_)

print("\nConclusion:")
print("K-Means clustering groups similar data points.")
print("Random noise increases variation in the dataset.")
print("The algorithm still identifies clusters using centroids.")