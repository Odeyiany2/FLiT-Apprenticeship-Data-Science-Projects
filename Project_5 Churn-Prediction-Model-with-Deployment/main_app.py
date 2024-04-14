import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt


st.set_page_config(page_title="Customer Churn Prediction App", page_icon="🏃🏽‍♀🏃🏼")

st.markdown("# 🏃🏽‍♀🏃🏼 Customer Churn Prediction for a Telecommunications Company")


# load the models 
model = joblib.load("Churn_Prediction_Model.joblib")
#model_2 = joblib.load("Telecom_Churn_Prediction_Model.joblib")


option = st.selectbox(
    "How would you like to analyze?",
    ("Entering customer's details manually", "Upload a csv file"))
if option == "Entering customer's details manually":
    gender = st.text_area("Enter the gender")
    partner = st.text_area("Does the customer have a partner?")
    dependents = st.text_area("Does the customer have dependents?")
    contract = st.text_area("Type of contract?")
    internet = st.text_area("Type of internet service used?")
    monthly = st.text_area("Enter monthly charges")
    total = st.text_area("Enter total charges")
    payment = st.text_area("Enter the payment method")
    device = st.text_area("Is device protection enabled?")
    tv = st.text_area("Is streaming TV enabled?")
    movies = st.text_area("Is streaming movies enabled?")
    backup = st.text_area("Is online backup enabled?")
    security = st.text_area("Is online security enabled?")
    tech = st.text_area("Is tech support enabled?")
    multiple = st.text_area("Is mulitple lines enabled?")
    senior = st.text_area("Is the customer a senior citizen?")
    phone = st.text_area("Is phone service enabled")
    billing = st.text_area("Is paperless billing enabled?")



    



























st.divider()
st.markdown("##### Built by Miriam Itopa Odeyiany as a Project for a Data Science Apprenticeship Program")
st.write("Copyright © Miriam Itopa Odeyiany, Nigeria 2024")