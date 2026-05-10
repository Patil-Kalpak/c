# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create dataset
data = {
    'Hours': [1,2,3,4,5,6,7,8],
    'Marks': [12,18,33,39,52,61,68,79]
}

# Convert dataset into dataframe
df = pd.DataFrame(data)

# Input and output
X = df[['Hours']]
y = df['Marks']

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict test values
y_pred = model.predict(X_test)

# Calculate RMSE
rmse = math.sqrt(mean_squared_error(y_test, y_pred))

# Print outputs
print("Actual Values:", list(y_test))
print("Predicted Values:", y_pred)
print("RMSE:", rmse)

# Predict all values for full graph
all_pred = model.predict(X)

# Scatter plot of actual data
plt.scatter(X, y, label="Actual Data")

# Regression line
plt.plot(X, all_pred, label="Regression Line")

# Labels and title
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Simple Linear Regression")

# Show legend
plt.legend()

# Show graph
plt.show()