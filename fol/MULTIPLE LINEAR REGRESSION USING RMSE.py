# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import math

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create non-linear realistic dataset
data = {
    'Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [60,68,72,75,81,84,91,96],
    'Marks': [14,20,36,40,58,62,73,88]
}

# Convert into dataframe
df = pd.DataFrame(data)

# Multiple input columns
X = df[['Hours', 'Attendance']]

# Output column
y = df['Marks']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict output for test data
y_pred = model.predict(X_test)

# Calculate RMSE
rmse = math.sqrt(mean_squared_error(y_test, y_pred))

# Print results
print("Actual Values:", list(y_test))
print("Predicted Values:", y_pred)
print("RMSE:", rmse)

# Predict all values for graph
all_pred = model.predict(X)

# Actual values plot
plt.plot(y.values, marker='o', label='Actual')

# Predicted values plot
plt.plot(all_pred, marker='o', label='Predicted')

# Labels and title
plt.xlabel("Data Points")
plt.ylabel("Marks")
plt.title("Multiple Linear Regression")

# Legend
plt.legend()

# Show graph
plt.show()