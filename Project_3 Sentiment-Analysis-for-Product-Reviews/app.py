import streamlit as st
import time
import pandas as pd
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
        st.write("Predicted Sentiment is: ", prediction)
        title = st.text_area(label="Output", value=translation, height=200, label_visibility="hidden")

elif option == "A csv file":
    file = st.file_uploader("Upload a csv file")
    #creating a function to perform our preprocessing of data
    def data_transform(data):
        corpus = [] 
        for item in data: 
            new_item = re.sub('[^a-zA-Z]',' ',str(item)) 
            new_item = new_item.lower() 
            new_item = new_item.split() 
            new_item = [wn.lemmatize(word) for word in new_item if word not in set(stopwords.words('english'))] 
            corpus.append(' '.join(str(x) for x in new_item)) 
        return corpus

    #function for analysis
    def analyze(x):
        if x >= 0.5:
            return "Positive"
        elif x <= -0.5:
            return "Negative"
        else:
            return "Neutral"
    if st.button("Predict"):
        start = time.time()
        df = pd.read_csv(file)
        corpus = data_transform(df["reviews"])
        new_corpus = cv.fit_transform(corpus)
        df["sentiment_score"] = model.predict(new_corpus)
        df["sentiment_analysis"] = df["sentiment_score"].apply(analyze)
        end = time.time()
        st.write(df.head())
        st.write("Prediction time taken: ", round(end-start, 2), "seconds.")





st.divider()
st.markdown("##### Built by Miriam Itopa Odeyiany for project 5 of my apprenticeship program")
st.write("Copyright © Miriam Itopa Odeyiany, Nigeria 2024")