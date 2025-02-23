
import pickle
import streamlit as st
import pandas as pd

# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# give the Streamlit app page a title
st.title("Customer Churn")

# input widget for getting user values for X (feature matrix value)
CustServCalls = st.slider("CustServCalls", min_value=0, max_value=9, value=3)
DayMins = st.slider("DayMins", min_value=0, max_value=351, value=70)
DataUsage = st.slider("DataUsage", min_value=0, max_value=6, value=3)

# After selesting CustServCalls, DayMins, DataUsage the user then submits the price value
if st.button("Predict"):
  # take the price value, and format the value the right way
  prediction = model.predict([[CustServCalls, DayMins, DataUsage]])[0].round(2)
  st.write("The customer is likely to", prediction, "in the coming quarter")
