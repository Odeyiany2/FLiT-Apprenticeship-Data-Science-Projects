import streamlit as st
import time
import pandas as pd
#import joblib
import matplotlib.pyplot as plt
# from sklearn.feature_extraction.text import CountVectorizer
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
#import re 
import cleantext

st.set_page_config(page_title="Amazon Reviews Sentiment Analyzer", page_icon="😊🙁")

st.markdown("# 😊🙁 Amazon Reviews Sentiment Analyzer")

#load model
#model = joblib.load("Amazon_Sentiment_Analysis_Model.joblib")

option = st.selectbox(
    "What would you like to analyze?",
    ("A text", "A csv file"))

if option=='A text':
    title = st.text_area("Enter your english text here?")
    #function for preprocessing 
    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity

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
        #cv = CountVectorizer(ngram_range = (1,2))
        text_score = score(title)
        prediction = analyze(text_score)
        end = time.time()
        st.write("Prediction time taken: ", round(end-start, 2), "seconds.")
        st.write("Polarity Score is: ", text_score)
        st.write("Predicted Sentiment is: ", prediction)
    

elif option == "A csv file":
    file = st.file_uploader("Upload a csv file")
    #creating a function to perform our preprocessing of data
    # # creating an object of WordNetLemmatizer
    # wn = WordNetLemmatizer()
    # def data_transform(data):
    #     corpus = [] 
    #     for item in data: 
    #         new_item = re.sub('[^a-zA-Z]',' ',str(item)) 
    #         new_item = new_item.lower() 
    #         new_item = new_item.split() 
    #         new_item = [wn.lemmatize(word) for word in new_item if word not in set(stopwords.words('english'))] 
    #         corpus.append(' '.join(str(x) for x in new_item)) 
    #     return corpus
    
    #function for preprocessing 
    def score(x):
        blob1 = TextBlob(str(x))
        return blob1.sentiment.polarity

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
        #corpus = data_transform(df["reviews"])
        #cv = CountVectorizer(ngram_range = (1,2))
        #new_corpus = cv.fit_transform(corpus)
        df["sentiment_score"] = df["reviews"].apply(score)
        df["sentiment_analysis"] = df["sentiment_score"].apply(analyze)
        end = time.time()
        st.write(df.head())
        
        #create a chart on the setiment analysis
        dict_ = dict(df["sentiment_analysis"].value_counts())
        explode = tuple(0.1 if i == 1 else 0 for i in range(len(dict_.values())))
        fig1, ax1 = plt.subplots()
        ax1.pie(dict_.values(), explode=explode, labels=dict_.keys(), autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')        
        st.pyplot(fig1)
        # Save the plot to a file (e.g., scatter.png)
        sentiment_chart = "sentiment_chart.png"
        plt.savefig(sentiment_chart)
        
        st.write("Prediction time taken: ", round(end-start, 2), "seconds.")

        #download button for the analyzed csv file
        @st.cache_data 
        def convert_df(df):
            return df.to_csv().encode("utf-8")
        csv = convert_df(df)
        
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='reviews sentiment.csv',
            mime='text/csv',
        )

        #download button for the chart image
        with open(sentiment_chart, "rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name=sentiment_chart,
                    mime="image/png"
                  )
else:
    st.write("Nothing was selected")








st.divider()
st.markdown("##### Built by Miriam Itopa Odeyiany as a Project for a Data Science Apprenticeship Program")
st.write("Copyright © Miriam Itopa Odeyiany, Nigeria 2024")