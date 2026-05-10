# Import pandas library for dataset handling
import pandas as pd
# Import matplotlib for plotting graph
import matplotlib.pyplot as plt
# Import make_regression for generating synthetic regression dataset
from sklearn.datasets import make_regression
# Import train_test_split for splitting dataset
from sklearn.model_selection import train_test_split
# Import Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor
# Import evaluation metrics
from sklearn.metrics import mean_squared_error,r2_score

# Generate synthetic regression dataset
X,y=make_regression(
# Total number of samples
n_samples=200,
# Total number of features
n_features=3,
# Add noise for realistic output
noise=15,
# Random state for same output every run
random_state=42
)

# Convert generated data into dataframe
df=pd.DataFrame(
X,
columns=['Feature1','Feature2','Feature3']
)

# Add target column
df['Price']=y

# Print dataset
print("\nDataset:\n")
print(df.head())

# Select input features
X=df[['Feature1','Feature2','Feature3']]

# Select target column
y=df['Price']

# Split dataset into training and testing data
X_train,X_test,y_train,y_test=train_test_split(
# Input data
X,
# Output data
y,
# 20% data for testing
test_size=0.2,
# Random state for same output every run
random_state=42
)

# Create Random Forest Regressor model
model=RandomForestRegressor(
# Number of decision trees
n_estimators=100,
# Random state for same output every run
random_state=42
)

# Train model
model.fit(X_train,y_train)

# Predict testing data
y_pred=model.predict(X_test)

# Calculate Mean Squared Error
mse=mean_squared_error(y_test,y_pred)

# Calculate R2 Score
r2=r2_score(y_test,y_pred)

# Print Mean Squared Error
print("\nMean Squared Error:",round(mse,2))

# Print R2 Score
print("R2 Score:",round(r2,2))

# Print actual and predicted values
print("\nActual vs Predicted Values:\n")

for actual,predicted in zip(y_test,y_pred):

    # Print actual and predicted value
    print("Actual:",round(actual,2),"Predicted:",round(predicted,2))

# Create graph
plt.figure()

# Plot actual values
plt.plot(y_test.values,marker='o',label='Actual')

# Plot predicted values
plt.plot(y_pred,marker='s',label='Predicted')

# Graph title
plt.title("Actual vs Predicted Values")

# X-axis label
plt.xlabel("Test Data")

# Y-axis label
plt.ylabel("Target Value")

# Show legend
plt.legend()

# Show graph
plt.show()