![picture](https://github.com/Odeyiany2/FLiT-Apprenticeship-Data-Science-Projects/blob/main/Project_3%20Sentiment-Analysis-for-Product-Reviews/ama.jpg)
# Sentiment Analysis for Product Reviews
For project 3, I will be performing a Natural Language Processing(NLP) workload by analyzing a dataset of product reviews for an E-commerce. 
The goal is to build a sentiment analysis model (this is a sub-field of NLP) that can classify reviews into: Positive or Negative.

## Tools 
The following tools were used for different areas of the project:
* Python Libraries:
  - `Pandas`: for data analysis and manipulation
  - `Seaborn`: a library based on matplotlib and it provides a high-level interface for data visualization
  - `matplotlib`: for data visualization
  - `word cloud`: for visualizing text data
    
* Natural Language Processing:
  - `nlkt`: Natural Language Toolkit is a collection of libraries for natural language processing
  - `stopwords`: a collection of words that don't provide any meaning to a dataset
  - `WordNetLemmatizer`: used to convert different forms of words into a single item but still keeping the context intact

* Scikit Learn (Python Machine Learning Library):
  - `CountVectorizer`: Transform text to vectors
  - `GridSearchCV`: Hyperparameter tuning
  - `RandomForestClassifier`: ML algorithm for classification problems
    
* Deployment: `Streamlit`

## Data Insights
With the use of pythonn libraries  `seaborn` and `matplotlib` to perform data visualization in the notebook, the following were discovered:
* More than 50% of the customers gave a positive review about the amazon product(s) they purchased. This proves that majority of the time,
  many of the customers are satisfied with their purchase.
* The business recorded its highest level of satisfied purchases due to the positive reviews left by the customers. The positive reviews surpassed the negative ones with a great margin. 
