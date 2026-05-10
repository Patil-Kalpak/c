# EXP 8 : EM Algorithm using Gaussian Mixture Model

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# ---------------------------------------------------
# Generate Synthetic Dataset
# ---------------------------------------------------

X, y = make_blobs(
    n_samples=300,
    centers=3,
    cluster_std=2,
    random_state=42
)

# Original Dataset
df = pd.DataFrame(X, columns=['Feature1', 'Feature2'])

print("Original Dataset:\n")
print(df.head())

# ---------------------------------------------------
# Visualization 1 : Original Dataset
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(X[:,0], X[:,1])

plt.title("Original Dataset")
plt.xlabel("Feature1")
plt.ylabel("Feature2")

plt.show()

# ---------------------------------------------------
# Add Random Noise
# ---------------------------------------------------

noise = np.random.normal(0, 2.5, X.shape)

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

plt.scatter(X_noisy[:,0], X_noisy[:,1])

plt.title("Noisy Dataset")
plt.xlabel("Feature1")
plt.ylabel("Feature2")

plt.show()

# ---------------------------------------------------
# Apply EM Algorithm
# ---------------------------------------------------

gmm = GaussianMixture(
    n_components=3,
    random_state=42
)

gmm.fit(X_noisy)

# Predict Clusters
clusters = gmm.predict(X_noisy)

# Cluster Centers
means = gmm.means_

print("\nCluster Centers:\n")
print(means)

# Probabilities
print("\nProbabilities of First 5 Points:\n")
print(gmm.predict_proba(X_noisy)[:5])

# ---------------------------------------------------
# Visualization 3 : EM Clustering
# ---------------------------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    X_noisy[:,0],
    X_noisy[:,1],
    c=clusters,
    cmap='viridis'
)

# Plot Cluster Centers
plt.scatter(
    means[:,0],
    means[:,1],
    s=250,
    marker='X'
)

plt.title("EM Clustering using GMM")
plt.xlabel("Feature1")
plt.ylabel("Feature2")

plt.show()

# ---------------------------------------------------
# Extra Information
# ---------------------------------------------------

print("\nNumber of Clusters :", gmm.n_components)

print("\nLog Likelihood :", gmm.score(X_noisy))

# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------

print("\nConclusion:")
print("EM performs probabilistic clustering.")
print("It uses Expectation and Maximization steps.")
print("The model can still cluster noisy data.")