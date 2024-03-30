import streamlit as st
import time
import pandas
import joblib

st.set_page_config(page_title="Amazon Reviews Sentiment Analyzer", page_icon="😊🙁")

st.markdown("# 😊🙁 Amazon Reviews Sentiment Analyzer")

#load model
model = joblib.load("Amazon_Sentiment_Analysis_Model.joblib")

option = st.selectbox(
    'What would you like to analyze?',
    ('A text', 'A csv file'))

if option=='A text':
    title = st.text_area('English Text', 'Enter your english text here?')
    if st.button('Predict'):
        with st.spinner(f"Translating text..."):
            translation = translate(dict_lang[language], title)

        st.write(f")
        title = st.text_area(label='Output', value=translation, height=200, label_visibility='hidden')







st.divider()
st.markdown("##### Built by Miriam Itopa Odeyiany as a project for an apprenticeship program. [FLiT Data Science Apprenticeship](https://github.com/Odeyiany2/FLiT-Apprenticeship-Data-Science-Projects) ")
st.write("Copyright © Miriam Itopa Odeyiany, Nigeria 2023")

