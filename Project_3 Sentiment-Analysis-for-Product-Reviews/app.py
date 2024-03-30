import streamlit as st
import time
import pandas
import joblib
from sklearn.feature_extraction.text import CountVectorizer

st.set_page_config(page_title="Amazon Reviews Sentiment Analyzer", page_icon="😊🙁")

st.markdown("# 😊🙁 Amazon Reviews Sentiment Analyzer")

#load model
model = joblib.load("Amazon_Sentiment_Analysis_Model.joblib")

option = st.selectbox(
    "What would you like to analyze?",
    ("A text", "A csv file"))

if option=="A text"
    title = st.text_area("Enter your english text here?")
    if st.button("Predict"):
        start = time.time()
        cv = CountVectorizer(ngram_range = (1,2))
        text = cv.fit_transform([title])
        prediction = model.predict(text)
        end = time.time()
        st.write("Prediction time taken: ", round(end-start, 2), "seconds.")
        title = st.text_area(label="Output", value=translation, height=200, label_visibility="hidden")

elif option == "A csv file"






st.divider()
st.markdown("##### Built by Miriam Itopa Odeyiany for project 5 of my apprenticeship program")
st.write("Copyright © Miriam Itopa Odeyiany, Nigeria 2024")