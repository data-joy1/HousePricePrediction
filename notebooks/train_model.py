# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pickle
import os

# Load dataset (you can replace this with an actual dataset)
# For now, let's create a sample dataset
data = {
    "sqft": [1400, 1600, 1700, 1875, 1100, 1550, 1230, 1420],
    "bedrooms": [3, 3, 3, 4, 2, 3, 2, 3],
    "bathrooms": [1, 2, 2, 2, 1, 2, 1, 2],
    "price": [200000, 250000, 270000, 290000, 180000, 240000, 190000, 210000]
}

# Convert dictionary to Pandas DataFrame
df = pd.DataFrame(data)

# Define features (X) and target variable (y)
X = df[['sqft', 'bedrooms', 'bathrooms']]
y = df['price']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f"Model Mean Absolute Error: ${mae:,.2f}")

# Ensure deployment folder exists
os.makedirs("../deployment", exist_ok=True)

# Save the trained model
with open("../deployment/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")