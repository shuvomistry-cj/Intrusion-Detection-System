import streamlit as st

# Move set_page_config to the first line
st.set_page_config(page_title="Intrusion Detection System", layout="wide")

import os
import joblib
import pandas as pd
import numpy as np

# Define paths
MODEL_PATH = "models/intrusion_model.pkl"
ENCODER_PATH = "models/label_encoders.pkl"
RESULTS_PATH = "results/test_predictions.csv"

# Create results directory if it doesn't exist
os.makedirs("results", exist_ok=True)

# Required columns from training data (excluding target column)
REQUIRED_COLUMNS = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 
                   'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 
                   'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 
                   'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 
                   'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 
                   'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 
                   'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 
                   'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 
                   'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 
                   'dst_host_serror_rate', 'dst_host_srv_serror_rate', 
                   'dst_host_rerror_rate', 'dst_host_srv_rerror_rate']

# Known categorical columns
CATEGORICAL_COLUMNS = ['protocol_type', 'service', 'flag']

# Load the model (check if it exists)
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    st.warning(" Model file not found! Train the model first.")
    model = None  # Prevents crashing

# Load encoders (required for preprocessing)
if os.path.exists(ENCODER_PATH):
    encoders = joblib.load(ENCODER_PATH)
else:
    st.warning(" Label encoders not found! Train the model first.")
    encoders = None

# Title
st.title("Intrusion Detection System")

# Upload test data
uploaded_file = st.file_uploader("Upload CSV file for prediction", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write(" Uploaded Data Preview:", data.head())
    
    # Show missing columns
    missing_cols = set(REQUIRED_COLUMNS) - set(data.columns)
    if missing_cols:
        st.warning(f" Missing columns in test data: {', '.join(missing_cols)}")
        st.info("These columns will be initialized with zeros.")

    if st.button("Predict"):
        if model is None or encoders is None:
            st.error(" Model or encoders not found. Please train the model first.")
        else:
            try:
                # Preprocess data using the same encoders
                data_processed = data.copy()
                
                # Add missing columns with zeros
                for col in REQUIRED_COLUMNS:
                    if col not in data_processed.columns:
                        data_processed[col] = 0
                
                # Ensure columns are in the same order as training
                data_processed = data_processed[REQUIRED_COLUMNS]
                
                # Handle missing values
                data_processed.fillna(0, inplace=True)
                
                # Apply label encoding to categorical columns
                for col in CATEGORICAL_COLUMNS:
                    if col in data_processed.columns:
                        # Convert to string to match training process
                        data_processed[col] = data_processed[col].astype(str)
                        if col in encoders:
                            # Handle unseen categories
                            known_categories = set(encoders[col].classes_)
                            data_processed[col] = data_processed[col].apply(
                                lambda x: x if x in known_categories else 'unknown'
                            )
                            try:
                                data_processed[col] = encoders[col].transform(data_processed[col])
                            except:
                                st.warning(f" New categories found in '{col}'. Treating them as 'unknown'.")
                                # For new categories, set to -1 or another special value
                                data_processed[col] = 0
                
                # Make predictions
                predictions = model.predict(data_processed)
                
                # Create a more informative results DataFrame
                results_df = pd.DataFrame({
                    "ID": range(len(predictions)),
                    "Prediction": predictions
                })
                
                # Display predictions with a better format
                st.write(" Predictions:")
                st.dataframe(results_df)
                
                # Save predictions
                results_df.to_csv(RESULTS_PATH, index=False)
                st.success(f" Predictions saved to '{RESULTS_PATH}'")
                
            except Exception as e:
                st.error(f" Error during prediction: {str(e)}")
                st.info(" Please check if your test data format matches the training data format")