import streamlit as st
import joblib 
import time


st.set_page_config(page_title="Reviews Sentiment Analysis App", page_icon="😊😟")
st.markdown("# 😊😟 Sentiment Analysis")
st.markdown("### (Is the review Positive or Negative?)")

#load model
model = joblib.load('Sentiment_Analysis_Model.joblib')

option = st.selectbox(
    'What would you like to translate?',
    ('A text', 'A csv file'))

review = st.text_input("Enter your review")
submit = st.button("Predict")

if submit:
    start = time.time()
    prediction = model.predict([review])
    end = time.time()
    st.write("Prediction time taken: ", round(end-start, 2), "seconds")
    print(prediction[0])
    st.write("Predicted Sentiment is: ", prediction[0])

