import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load("best_gradient_boosting_model.pkl")

st.title("🌍 Travel Package Price Prediction App")
st.write("Predict tour package prices using Machine Learning (Gradient Boosting Regressor).")

# Define input fields
Days = st.number_input("Number of Days", min_value=1, max_value=30, value=5)
Nights = st.number_input("Number of Nights", min_value=1, max_value=30, value=4)
Discount = st.number_input("Discount (%)", min_value=0, max_value=100, value=10)
Has_Positive_Word = st.selectbox("Has Positive Word in Title?", ["Yes", "No"])
Destination = st.text_input("Destination", "Goa")
Package_Type = st.selectbox("Package Type", ["Family", "Honeymoon", "Adventure", "Wildlife", "Beach"])
City = st.text_input("City", "Mumbai")

# Activity-based binary inputs
Adventure = st.selectbox("Adventure?", [0, 1])
Sightseeing = st.selectbox("Sightseeing?", [0, 1])
Nature = st.selectbox("Nature?", [0, 1])
Beach = st.selectbox("Beach?", [0, 1])
Romantic = st.selectbox("Romantic?", [0, 1])
Luxury = st.selectbox("Luxury?", [0, 1])
Wildlife = st.selectbox("Wildlife?", [0, 1])
Hill = st.selectbox("Hill?", [0, 1])
Historical = st.selectbox("Historical?", [0, 1])
Water = st.selectbox("Water?", [0, 1])
Cultural = st.selectbox("Cultural?", [0, 1])
Trekking = st.selectbox("Trekking?", [0, 1])

# Prepare input for model
input_data = pd.DataFrame([[
    Days, Nights, Discount, Has_Positive_Word, Destination, Package_Type, City,
    Adventure, Sightseeing, Nature, Beach, Romantic, Luxury, Wildlife,
    Hill, Historical, Water, Cultural, Trekking
]], columns=[
    'Days', 'Nights', 'Discount', 'Has_Positive_Word', 'Destination', 'Package_Type', 'City',
    'Adventure', 'Sightseeing', 'Nature', 'Beach', 'Romantic', 'Luxury', 'Wildlife',
    'Hill', 'Historical', 'Water', 'Cultural', 'Trekking'
])

# Convert Yes/No to 1/0
input_data['Has_Positive_Word'] = input_data['Has_Positive_Word'].map({'Yes': 1, 'No': 0})

# Predict
if st.button("Predict Package Price"):
    prediction = model.predict(input_data)[0]
    st.success(f" Predicted Tour Package Price: ₹{prediction:,.2f}")
