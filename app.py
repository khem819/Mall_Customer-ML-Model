import streamlit as st
import numpy as np
import joblib


kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🛍️ Customer Segmentation App")
st.write("Enter customer details to predict the segment.")

Gender = st.selectbox("Gender", ["Male", "Female"])
Age = st.number_input("Age", 18, 100)
Annual_Income = st.number_input("Annual Income (k$)", 0, 200)
Spending_Score = st.number_input("Spending Score (1-100)", 0, 100)

if st.button("Predict Segment"):

    gender = 0 if Gender == "Male" else 1
    input_data = np.array([[gender, Age, Annual_Income, Spending_Score]])
    input_scaled = scaler.transform(input_data)
    cluster = kmeans.predict(input_scaled)[0]

    st.success(f"🎯 Predicted Segment: Cluster {cluster}")