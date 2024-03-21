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
  - `Joblib`: Saving our model for deployment
    
* Natural Language Processing:
  - `nlkt`: Natural Language Toolkit is a collection of libraries for natural language processing
  - `stopwords`: a collection of words that don't provide any meaning to a dataset
  - `WordNetLemmatizer`: used to convert different forms of words into a single item but still keeping the context intact

* Scikit Learn (Python Machine Learning Library):
  - `CountVectorizer`: Transform text to vectors
  - `GridSearchCV`: Hyperparameter tuning
  - `RandomForestClassifier`: ML algorithm for classification problems

* Evaluation Metrics:
  - `Accuracy Score`: Number of correctly predicted class over the total classes 
  - `Precision`: ratio of correctly predicted positive classes over the total positive classes
  - `Recall`: ratio of correctly predicted positive class over the total classes
  - `Classification report`: a report showing precision, recall and F-1 score 
  - `ROC Curve`: a plot showing the true positive rate(TPR) over false positive rate(FPR)
  - `Confusion matrix`: a table for assessing the quality of our classification model prediction
    
* Deployment: `Streamlit`

## Data Insights
With the use of python libraries  `seaborn` and `matplotlib` to perform data visualization (Univariate and Bivariate Analysis) in the notebook, the following were discovered:
* Amazon products on a scale of 1-5, with one being bad and 5 being excellent, have a 65% of excellent ratings.
* The 5 star rating for products increased massively in the year 2015.
* Positive sentiments also garnered much percentage than that of the negative sentiments-84% for positive and 16% for negative. There is also a massive increase in positive sentiments in the year 2015.
* In all 2015, showed that customers were pleased with their purchases.
* **One important conclusion from our visualization is that our dataset is highly imbalanced so we will be using algorithms and techniques that effectively takes care of this imbalance and maintains our models' accuracy.**

## Model Evaluation Metrics
Intially the stats pf the models' evaluation was as follows:
  - We got an accuracy of 85%
  - A precision score of over 85%: this means our model predicted 85% of positive labels in our dataset correctly. 
  - Our recall score of 99%

After introducing the use of stop words, our stats improved better
  - Accuracy score became 88%


## NoteBook Structure
```bash
├── Downloading and Importing of Necessary Libraries
├── Data Collection
├── Exploratory Data Analysis
│   ├── converting columns to date data types
│   ├── treating missing data
│   ├── creating new columns
├── Data Visualization
├── Data Preprocessing
├── Model Building 
│   ├── model training
│   ├── model evaluation
│   ├── model saving
```



## Problems Encountered and how they were solved
When saving the model built so it can be incorporated into the streamlit application, I kept getting an error that the size of the model 
has exceeded the github file size limit. I later figured that I needed to incorporate the Github Large File Storage (LFS) so that after saving my model I can easily push my changes to my github repo without any issues. 

### **Resources to learn more about Git LFS**
* [Learn more about Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage)
* [Watch this video](https://youtu.be/jXsvFfksvd0?si=cL95OQ6j_g5ivcr3)
