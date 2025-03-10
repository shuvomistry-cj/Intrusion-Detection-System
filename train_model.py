import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import os

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/Train_data.csv")

# Check for missing values
df.fillna(0, inplace=True)  # Replace missing values with 0

# Define known categorical columns
categorical_cols = ['protocol_type', 'service', 'flag', 'xAttack']

# Convert categorical columns to numeric using Label Encoding
label_encoders = {}
for col in categorical_cols:
    if col in df.columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le  # Store encoders for future use

# Save the encoders (for test data processing later)
joblib.dump(label_encoders, "models/label_encoders.pkl")

# Split dataset into features (X) and target (y)
X = df.iloc[:, :-1]  # Features (all columns except last)
y = df.iloc[:, -1]   # Target (last column)

# Split into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Validate model
y_pred = model.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
print(f"Validation Accuracy: {accuracy:.2f}")

# Save trained model
joblib.dump(model, "models/intrusion_model.pkl")
print("Model saved successfully!")
