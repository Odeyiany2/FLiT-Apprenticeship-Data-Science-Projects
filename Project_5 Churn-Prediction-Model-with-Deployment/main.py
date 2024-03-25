import streamlit as st
import joblib
import time


st.set_page_config(page_title="Customer Churn Prediction App", page_icon="🏃🏽‍♀🏃🏽")
st.markdown("# 🏃🏽‍♀🏃🏽 Customer Churn Prediction") 

#load model
model = joblib.load('Churn_Prediction_Model.joblib')
