import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt


st.set_page_config(page_title="Customer Churn Prediction App", page_icon="🏃🏽‍♀🏃🏼")

st.markdown("# 🏃🏽‍♀🏃🏼 Customer Churn Prediction for a Telecom Company")


# load the models 
model = joblib.load('Churn_Prediction_Model.joblib')
model_2 = joblib.load("Telecom_Churn_Prediction_Model.joblib")


option = st.selectbox(
    "How would you like to analyze?",
    ("Entering customer's details manually", "UploadinA csv file"))
if st.button("Predict"):
    start = time.time()
    



























st.divider()
st.markdown("##### Built by Miriam Itopa Odeyiany as a Project for a Data Science Apprenticeship Program")
st.write("Copyright © Miriam Itopa Odeyiany, Nigeria 2024")