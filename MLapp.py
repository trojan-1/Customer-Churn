import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load the scaler (if used during training)
try:
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    use_scaler = True
except FileNotFoundError:
    scaler = None
    use_scaler = False

# Streamlit app title
st.title("Customer Churn Prediction")

# Input widgets for user input
CustServCalls = st.slider("Customer Service Calls", min_value=0, max_value=9, value=3)
DayMins = st.slider("Day Mins", min_value=0, max_value=351, value=70)
DataUsage = st.slider("Data Usage (GB)", min_value=0, max_value=6, value=3)

# Convert inputs into a DataFrame (matching model feature names)
input_data = np.array([[CustServCalls, DayMins, DataUsage]])

# Apply the same scaling used in training
if use_scaler:
    input_data = scaler.transform(input_data)

# Prediction only when button is clicked
if st.button("Predict"):
    prediction = model.predict(input_data)[0]  # Get prediction

    # Convert to human-readable output
    prediction_labels = {0: "stay", 1: "leave"}
    result = prediction_labels.get(prediction, "Unknown")

    # Display result
    st.write(f"📌 The customer is likely to **{result}** in the coming quarter.")

