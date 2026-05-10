# Import numpy library
import numpy as np
# Import pandas library for dataset handling
import pandas as pd
# Import matplotlib for plotting graphs
import matplotlib.pyplot as plt

# Import train_test_split for splitting dataset
from sklearn.model_selection import train_test_split

# Import StandardScaler for feature scaling
from sklearn.preprocessing import StandardScaler

# Import KNN classifier
from sklearn.neighbors import KNeighborsClassifier

# Import evaluation metrics
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score

# Create dataset using dictionary
data={

# Age feature
"Age":[22,25,47,52,46,23,40,35,30,27,29,50,48,33,38,26,45,31,28,42],

# Annual Income feature
"AnnualIncome":[25,30,70,60,65,28,62,58,40,35,42,68,72,45,55,32,66,48,38,63],

# Spending Score feature
"SpendingScore":[50,55,48,52,45,53,50,54,52,56,49,47,51,53,50,55,48,54,56,49],

# Online Time feature
"OnlineTime":[6,7,5,6,6,7,6,6,7,8,6,5,5,7,6,8,6,7,8,6],

# Target column
"Purchase":["Yes","No","No","Yes","No","Yes","No","Yes","No","Yes",
             "Yes","No","Yes","Yes","No","Yes","No","No","Yes","No"]
}

# Convert dictionary into dataframe
df=pd.DataFrame(data)

# Print original dataset
print("\nOriginal Dataset:\n")
print(df)

# Convert target values into numerical values
# Yes = 1 and No = 0
df["Purchase"]=df["Purchase"].map({
"Yes":1,
"No":0
})

# Select input features
X=df[["Age","AnnualIncome","SpendingScore","OnlineTime"]]

# Select output column
y=df["Purchase"]

# Split dataset into training and testing data
X_train,X_test,y_train,y_test=train_test_split(
# Input data
X,
# Output data
y,
# 40% data for testing
test_size=0.4,
# Random state for same output every run
random_state=7,
# Maintain class balance
stratify=y
)

# Create scaler object
scaler=StandardScaler()

# Apply scaling on training data
X_train_scaled=scaler.fit_transform(X_train)

# Apply scaling on testing data
X_test_scaled=scaler.transform(X_test)

# Different K values
k_values=[1,3,5,7,9]

# Store training accuracies
train_accuracies=[]

# Store testing accuracies
test_accuracies=[]

# Print heading
print("\nModel Performance for Different K values:\n")

# Try different K values
for k in k_values:

    # Create KNN model
    knn=KNeighborsClassifier(
    # Number of neighbors
    n_neighbors=k,
    # Distance metric
    metric="euclidean"
    )

    # Train model
    knn.fit(X_train_scaled,y_train)

    # Predict training data
    y_train_pred=knn.predict(X_train_scaled)

    # Predict testing data
    y_test_pred=knn.predict(X_test_scaled)

    # Calculate training accuracy
    train_acc=accuracy_score(y_train,y_train_pred)

    # Calculate testing accuracy
    test_acc=accuracy_score(y_test,y_test_pred)

    # Calculate precision
    prec=precision_score(y_test,y_test_pred,zero_division=0)

    # Calculate recall
    rec=recall_score(y_test,y_test_pred,zero_division=0)

    # Calculate F1-score
    f1=f1_score(y_test,y_test_pred,zero_division=0)

    # Store training accuracy
    train_accuracies.append(train_acc)

    # Store testing accuracy
    test_accuracies.append(test_acc)

    # Print results for each K
    print(f"K = {k}")
    print(f"Training Accuracy : {train_acc:.2f}")
    print(f"Testing Accuracy  : {test_acc:.2f}")
    print(f"Precision         : {prec:.2f}")
    print(f"Recall            : {rec:.2f}")
    print(f"F1-Score          : {f1:.2f}")
    print("-"*40)

# Plot graph between K value and Testing Accuracy
plt.figure()

# Plot graph
plt.plot(k_values,test_accuracies,marker='o')

# X-axis label
plt.xlabel("K Value")

# Y-axis label
plt.ylabel("Testing Accuracy")

# Graph title
plt.title("Accuracy vs K")

# Show graph
plt.show()

# Plot graph for Training vs Testing Accuracy
plt.figure()

# Plot training accuracy
plt.plot(k_values,train_accuracies,marker='o',label="Training Accuracy")

# Plot testing accuracy
plt.plot(k_values,test_accuracies,marker='s',label="Testing Accuracy")

# X-axis label
plt.xlabel("K Value")

# Y-axis label
plt.ylabel("Accuracy")

# Graph title
plt.title("Training vs Testing Accuracy")

# Show legend
plt.legend()

# Show graph
plt.show()

# Find best K value automatically
optimal_k=k_values[test_accuracies.index(max(test_accuracies))]

# Print best K value
print("\nOptimal K Value:",optimal_k)

# Create final KNN model using best K
knn_optimal=KNeighborsClassifier(
# Best K value
n_neighbors=optimal_k,
# Distance metric
metric="euclidean"
)

# Train final model
knn_optimal.fit(X_train_scaled,y_train)

# Predict testing data
y_pred_optimal=knn_optimal.predict(X_test_scaled)

# Generate confusion matrix
cm=confusion_matrix(y_test,y_pred_optimal)

# Plot confusion matrix
plt.figure()

# Display confusion matrix
plt.imshow(cm,cmap="Blues")

# Graph title
plt.title(f"Confusion Matrix (K = {optimal_k})")

# X-axis label
plt.xlabel("Predicted Label")

# Y-axis label
plt.ylabel("Actual Label")

# Show color bar
plt.colorbar()

# Display values inside confusion matrix
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):

        # Show matrix value
        plt.text(j,i,cm[i,j],ha="center",va="center")

# Show graph
plt.show()