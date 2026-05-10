# Import pandas library for dataset handling
import pandas as pd
# Import matplotlib for plotting graph
import matplotlib.pyplot as plt
# Import train_test_split for splitting dataset
from sklearn.model_selection import train_test_split
# Import Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor
# Import evaluation metrics
from sklearn.metrics import mean_squared_error,r2_score

# Create house price dataset using dictionary
data={

# Area feature
'Area':[1000,1200,1500,1800,2000,2200,2500,2700,3000,3200,
        1100,1400,1600,1900,2100,2400,2600,2900,3100,3300],

# Number of bedrooms
'Bedrooms':[2,2,3,3,4,4,4,5,5,5,
            2,3,3,4,4,4,5,5,5,6],

# House age feature
'HouseAge':[10,8,7,6,5,4,4,3,2,2,
            9,8,7,5,5,4,3,2,2,1],

# Price target column
'Price':[50,58,63,75,79,88,91,103,109,121,
         54,61,70,76,85,90,96,106,117,123]
}

# Convert dictionary into dataframe
df=pd.DataFrame(data)

# Print dataset
print("\nDataset:\n")
print(df)

# Select input features
X=df[['Area','Bedrooms','HouseAge']]

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
    print("Actual:",actual,"Predicted:",round(predicted,2))

# Create graph
plt.figure()

# Plot actual values
plt.plot(y_test.values,marker='o',label='Actual')

# Plot predicted values
plt.plot(y_pred,marker='s',label='Predicted')

# Graph title
plt.title("Actual vs Predicted House Prices")

# X-axis label
plt.xlabel("Test Data")

# Y-axis label
plt.ylabel("House Price")

# Show legend
plt.legend()

# Show graph
plt.show()