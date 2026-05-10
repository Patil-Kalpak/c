# Import pandas library for dataset handling
import pandas as pd
# Import matplotlib for plotting graphs
import matplotlib.pyplot as plt
# Import make_classification for generating synthetic dataset
from sklearn.datasets import make_classification
# Import train_test_split for splitting dataset
from sklearn.model_selection import train_test_split
# Import Decision Tree Classifier model
from sklearn.tree import DecisionTreeClassifier
# Import evaluation metrics
from sklearn.metrics import accuracy_score,log_loss

# Generate synthetic classification dataset
X,y=make_classification(
# Total number of samples
n_samples=200,
# Total number of features
n_features=4,
# Number of informative features
n_informative=3,
# Number of redundant features
n_redundant=0,
# Number of output classes
n_classes=2,
# Add slight noise for realistic output
flip_y=0.08,
# Random state for same output every run
random_state=42
)

# Convert generated data into dataframe
df=pd.DataFrame(
X,
columns=['Feature1','Feature2','Feature3','Feature4']
)

# Add target column
df['Buy_Product']=y

# Print dataset
print("\nDataset:\n")
print(df.head())

# Select input features
X=df[['Feature1','Feature2','Feature3','Feature4']]

# Select output column
y=df['Buy_Product']

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

# Create Decision Tree model
model=DecisionTreeClassifier(
# Use entropy for information gain
criterion='entropy',
# Maximum depth of tree
max_depth=3,
# Minimum samples required to split
min_samples_split=4,
# Minimum samples required in leaf node
min_samples_leaf=2,
# Random state for same output every run
random_state=42
)

# Train the model
model.fit(X_train,y_train)

# Predict training data
train_pred=model.predict(X_train)

# Predict testing data
test_pred=model.predict(X_test)

# Calculate training accuracy
train_acc=accuracy_score(y_train,train_pred)

# Calculate testing accuracy
test_acc=accuracy_score(y_test,test_pred)

# Predict probabilities for training data
train_prob=model.predict_proba(X_train)

# Predict probabilities for testing data
test_prob=model.predict_proba(X_test)

# Calculate training loss
train_loss=log_loss(y_train,train_prob)

# Calculate testing loss
test_loss=log_loss(y_test,test_prob)

# Print training accuracy
print("\nTraining Accuracy:",round(train_acc,2))

# Print testing accuracy
print("Testing Accuracy:",round(test_acc,2))

# Print training loss
print("Training Loss:",round(train_loss,2))

# Print testing loss
print("Testing Loss:",round(test_loss,2))

# Store accuracy values
accuracy_values=[train_acc,test_acc]

# Labels for accuracy graph
accuracy_labels=['Training Accuracy','Testing Accuracy']

# Create accuracy graph
plt.figure()

# Plot accuracy graph
plt.bar(accuracy_labels,accuracy_values)

# Graph title
plt.title("Training vs Testing Accuracy")

# Y-axis label
plt.ylabel("Accuracy")

# Show graph
plt.show()

# Store loss values
loss_values=[train_loss,test_loss]

# Labels for loss graph
loss_labels=['Training Loss','Testing Loss']

# Create loss graph
plt.figure()

# Plot loss graph
plt.bar(loss_labels,loss_values)

# Graph title
plt.title("Training vs Testing Loss")

# Y-axis label
plt.ylabel("Loss")

# Show graph
plt.show()