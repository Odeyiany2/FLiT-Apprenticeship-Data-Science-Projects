import streamlit as st
import pandas as pd
import joblib


st.set_page_config(page_title="Customer Churn Prediction App", page_icon="😊🙁")

st.markdown("# 😊🙁 Customer Churn Prediction")










# load the models 
model = joblib.load('Churn_Prediction_Model.joblib')
model_2 = joblib.load("Telecom_Churn_Prediction_Model.joblib")

