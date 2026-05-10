# Sample example:
# Given a dataset containing features such as Age, Income,
# Student Status, and Credit Rating, build a Decision Tree
# model to predict whether a customer will Buy a Product (Yes/No).

# Accuracy as a performance measure is expected on
# training and testing dataset

# Import pandas library for dataset handling
import pandas as pd

# Import matplotlib for plotting graphs
import matplotlib.pyplot as plt

# Import train_test_split for splitting dataset
from sklearn.model_selection import train_test_split

# Import Decision Tree Classifier model
from sklearn.tree import DecisionTreeClassifier

# Import LabelEncoder for converting text into numbers
from sklearn.preprocessing import LabelEncoder

# Import evaluation metrics
from sklearn.metrics import accuracy_score, log_loss

# Create balanced dataset using dictionary
data = {

    # Age feature
    'Age': [
        'Young','Young','Middle','Old','Old',
        'Middle','Young','Old','Middle','Young',
        'Old','Middle','Young','Old','Middle',
        'Young','Old','Middle','Young','Old'
    ],

    # Income feature
    'Income': [
        'High','High','Medium','Low','Medium',
        'Medium','Low','High','Low','Medium',
        'High','Low','Medium','Medium','High',
        'Low','High','Medium','Low','Medium'
    ],

    # Student feature
    'Student': [
        'No','No','Yes','Yes','Yes',
        'No','Yes','No','Yes','No',
        'Yes','No','Yes','No','Yes',
        'No','Yes','No','Yes','No'
    ],

    # Credit Rating feature
    'Credit_Rating': [
        'Fair','Excellent','Fair','Excellent','Fair',
        'Fair','Excellent','Fair','Excellent','Fair',
        'Excellent','Fair','Excellent','Fair','Excellent',
        'Fair','Excellent','Fair','Excellent','Fair'
    ],

    # Target column
    'Buy_Product': [
        'No','No','Yes','Yes','Yes',
        'Yes','No','No','Yes','No',
        'Yes','Yes','No','Yes','Yes',
        'No','Yes','Yes','No','Yes'
    ]
}

# Convert dictionary into dataframe
df = pd.DataFrame(data)

# Create LabelEncoder object
le = LabelEncoder()

# Convert Age column into numerical values
df['Age'] = le.fit_transform(df['Age'])

# Convert Income column into numerical values
df['Income'] = le.fit_transform(df['Income'])

# Convert Student column into numerical values
df['Student'] = le.fit_transform(df['Student'])

# Convert Credit Rating column into numerical values
df['Credit_Rating'] = le.fit_transform(df['Credit_Rating'])

# Convert target column into numerical values
df['Buy_Product'] = le.fit_transform(df['Buy_Product'])

# Select input features
X = df[['Age', 'Income', 'Student', 'Credit_Rating']]

# Select output column
y = df['Buy_Product']

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(

    # Input data
    X,

    # Output data
    y,

    # 20% data for testing
    test_size=0.2,

    # Random state for same output every run
    random_state=42,

    # Maintain class balance in train and test data
    stratify=y
)

# Create Decision Tree model
model = DecisionTreeClassifier(

    # Use entropy for information gain
    criterion='entropy',

    # Maximum depth of tree
    max_depth=2,

    # Minimum samples required to split
    min_samples_split=4,

    # Minimum samples required in leaf node
    min_samples_leaf=2,

    # Random state for same output every run
    random_state=42
)

# Train the model using training data
model.fit(X_train, y_train)

# Predict training data
train_pred = model.predict(X_train)

# Predict testing data
test_pred = model.predict(X_test)

# Calculate training accuracy
train_acc = accuracy_score(y_train, train_pred)

# Calculate testing accuracy
test_acc = accuracy_score(y_test, test_pred)

# Predict probabilities for training data
train_prob = model.predict_proba(X_train)

# Predict probabilities for testing data
test_prob = model.predict_proba(X_test)

# Calculate training loss
train_loss = log_loss(y_train, train_prob)

# Calculate testing loss
test_loss = log_loss(y_test, test_prob)

# Print training accuracy
print("Training Accuracy:", round(train_acc, 2))

# Print testing accuracy
print("Testing Accuracy:", round(test_acc, 2))

# Print training loss
print("Training Loss:", round(train_loss, 2))

# Print testing loss
print("Testing Loss:", round(test_loss, 2))

# Store accuracy values
accuracy_values = [train_acc, test_acc]

# Labels for accuracy graph
accuracy_labels = ['Training Accuracy', 'Testing Accuracy']

# Plot accuracy bar graph
plt.bar(accuracy_labels, accuracy_values)

# Graph title
plt.title("Training vs Testing Accuracy")

# Y-axis label
plt.ylabel("Accuracy")

# Show graph
plt.show()

# Store loss values
loss_values = [train_loss, test_loss]

# Labels for loss graph
loss_labels = ['Training Loss', 'Testing Loss']

# Plot loss bar graph
plt.bar(loss_labels, loss_values)

# Graph title
plt.title("Training vs Testing Loss")

# Y-axis label
plt.ylabel("Loss")

# Show graph
plt.show()