import streamlit as st
import pandas as pd
import joblib


st.set_page_config(page_title="Customer Churn Prediction App", page_icon="🏃🏽‍♀🏃🏼")

st.markdown("# 🏃🏽‍♀🏃🏼 Customer Churn Prediction for a Telecom Company")


# load the models 
model = joblib.load('Churn_Prediction_Model.joblib')
model_2 = joblib.load("Telecom_Churn_Prediction_Model.joblib")


option = st.file_uploader("Upload a csv file")
if st.button("Predict"):



























st.divider()
st.markdown("##### Built by Miriam Itopa Odeyiany as a Project for a Data Science Apprenticeship Program")
st.write("Copyright © Miriam Itopa Odeyiany, Nigeria 2024")