# Import pandas library for dataset handling
import pandas as pd
# Import matplotlib for plotting graph
import matplotlib.pyplot as plt
# Import make_classification for generating synthetic dataset
from sklearn.datasets import make_classification
# Import train_test_split for splitting dataset
from sklearn.model_selection import train_test_split
# Import Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
# Import evaluation metrics
from sklearn.metrics import accuracy_score,confusion_matrix

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
df['Survived']=y

# Print dataset
print("\nDataset:\n")
print(df.head())

# Select input features
X=df[['Feature1','Feature2','Feature3','Feature4']]

# Select output column
y=df['Survived']

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

# Create Random Forest model
model=RandomForestClassifier(
# Number of decision trees
n_estimators=100,
# Random state for same output every run
random_state=42
)

# Train Random Forest model
model.fit(X_train,y_train)

# Predict testing data
y_pred=model.predict(X_test)

# Calculate accuracy
accuracy=accuracy_score(y_test,y_pred)

# Generate confusion matrix
cm=confusion_matrix(y_test,y_pred)

# Print accuracy
print("\nAccuracy:",round(accuracy,2))

# Print confusion matrix
print("\nConfusion Matrix:")
print(cm)

# Plot confusion matrix
plt.figure()

# Display confusion matrix
plt.imshow(cm,cmap='Blues')

# Graph title
plt.title("Random Forest Confusion Matrix")

# X-axis label
plt.xlabel("Predicted")

# Y-axis label
plt.ylabel("Actual")

# Show color bar
plt.colorbar()

# Display values inside confusion matrix
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):

        # Show matrix value
        plt.text(j,i,cm[i,j],ha='center',va='center',color='black')

# Show graph
plt.show()