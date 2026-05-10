# Import pandas library for dataset handling
import pandas as pd
# Import matplotlib for plotting graph
import matplotlib.pyplot as plt
# Import train_test_split for splitting dataset
from sklearn.model_selection import train_test_split
# Import Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
# Import LabelEncoder for converting text into numbers
from sklearn.preprocessing import LabelEncoder
# Import evaluation metrics
from sklearn.metrics import accuracy_score,confusion_matrix

# Create Titanic-like dataset using dictionary
data={

# Passenger class feature
'Pclass':[1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3],

# Gender feature
'Sex':['male','female','female','male','male',
       'female','female','male','female','male',
       'female','male','female','male','female',
       'male','female','male','female','male'],

# Age feature
'Age':[22,38,26,35,28,30,19,40,29,45,
       25,32,21,50,27,48,24,33,20,41],

# Fare feature
'Fare':[72,8,13,53,7,15,80,6,12,50,
        9,14,78,5,11,60,10,16,75,7],

# Target column
'Survived':['No','Yes','Yes','Yes','No',
            'Yes','Yes','No','Yes','No',
            'Yes','No','Yes','No','Yes',
            'Yes','Yes','No','Yes','No']
}

# Convert dictionary into dataframe
df=pd.DataFrame(data)

# Print dataset
print("\nDataset:\n")
print(df)

# Create LabelEncoder object
le=LabelEncoder()

# Convert gender into numerical values
df['Sex']=le.fit_transform(df['Sex'])

# Convert target column into numerical values
# No = 0 and Yes = 1
df['Survived']=df['Survived'].map({
'No':0,
'Yes':1
})

# Select input features
X=df[['Pclass','Sex','Age','Fare']]

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