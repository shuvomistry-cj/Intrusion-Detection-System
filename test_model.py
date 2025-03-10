import os
import pandas as pd
import joblib

# Load trained model and encoders
model = joblib.load("models/intrusion_model.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")

# Load test dataset
df_test = pd.read_csv("data/test_data.csv")

# Remove unwanted columns (like extra index columns)
df_test = df_test.loc[:, ~df_test.columns.str.contains('Unnamed', case=False)]

# Handle missing values
df_test.fillna(0, inplace=True)

# Encode categorical features using the saved label encoders
for col in label_encoders:
    if col in df_test.columns:
        df_test[col] = label_encoders[col].transform(df_test[col])

# Select features (assuming last column is target, exclude it if needed)
X_test = df_test.iloc[:, :-1]

# Predict
predictions = model.predict(X_test)

# Add predictions to dataframe
df_test["Prediction"] = predictions

# ✅ Ensure 'results' directory exists
os.makedirs("results", exist_ok=True)

# Save results
df_test.to_csv("results/test_predictions.csv", index=False)
print("✅ Predictions saved to 'results/test_predictions.csv'!")
