# Import matplotlib for plotting graphs
import matplotlib.pyplot as plt
# Import make_classification for generating synthetic dataset
from sklearn.datasets import make_classification
# Import train_test_split for splitting dataset
from sklearn.model_selection import train_test_split
# Import SVC for Support Vector Machine
from sklearn.svm import SVC
# Import evaluation metrics
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score
# Import StandardScaler for feature scaling
from sklearn.preprocessing import StandardScaler

# Generate synthetic classification dataset
X,y=make_classification(
# Total number of samples
n_samples=500,
# Total number of features
n_features=2,
# Number of informative features
n_informative=2,
# Number of redundant features
n_redundant=0,
# Number of output classes
n_classes=2,
# Distance between classes
class_sep=2.0,
# Random state for same output every run
random_state=42
)

# Create figure for dataset visualization
plt.figure()

# Plot class 0 points
plt.scatter(X[y==0,0],X[y==0,1],label="Class 0")

# Plot class 1 points
plt.scatter(X[y==1,0],X[y==1,1],label="Class 1")

# X-axis label
plt.xlabel("Feature 1")

# Y-axis label
plt.ylabel("Feature 2")

# Graph title
plt.title("Linearly Separable Synthetic Dataset")

# Show legend
plt.legend()

# Show graph
plt.show()

# Split dataset into training and testing data
X_train,X_test,y_train,y_test=train_test_split(
# Input data
X,
# Output data
y,
# 20% data for testing
test_size=0.2,
# Random state for same output every run
random_state=42,
# Maintain class balance
stratify=y
)

# Create scaler object
scaler=StandardScaler()

# Apply scaling on training data
X_train=scaler.fit_transform(X_train)

# Apply scaling on testing data
X_test=scaler.transform(X_test)

# Create Linear SVM model
svm_model=SVC(
# Use linear kernel
kernel='linear'
)

# Train SVM model
svm_model.fit(X_train,y_train)

# Predict testing data
y_pred=svm_model.predict(X_test)

# Calculate accuracy
accuracy=accuracy_score(y_test,y_pred)

# Generate confusion matrix
conf_matrix=confusion_matrix(y_test,y_pred)

# Calculate precision
precision=precision_score(y_test,y_pred)

# Calculate recall
recall=recall_score(y_test,y_pred)

# Print accuracy
print("Accuracy:",round(accuracy,2))

# Print confusion matrix
print("\nConfusion Matrix:\n",conf_matrix)

# Print precision
print("\nPrecision:",round(precision,2))

# Print recall
print("Recall:",round(recall,2))

# Create figure for confusion matrix
plt.figure()

# Display confusion matrix
plt.imshow(conf_matrix,cmap="Blues")

# X-axis label
plt.xlabel("Predicted")

# Y-axis label
plt.ylabel("Actual")

# Graph title
plt.title("Confusion Matrix")

# Show color bar
plt.colorbar()

# Display values inside confusion matrix
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):

        # Show matrix value
        plt.text(j,i,conf_matrix[i,j],ha="center",va="center",color="black")

# Show graph
plt.show()