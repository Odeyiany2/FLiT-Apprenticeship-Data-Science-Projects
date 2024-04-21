![picture](https://github.com/Odeyiany2/FLiT-Apprenticeship-Data-Science-Projects/blob/main/Project_3%20Sentiment-Analysis-for-Product-Reviews/ama.jpg)
# Sentiment Analysis for Product Reviews
For project 3, I will be performing a Natural Language Processing(NLP) workload by analyzing a dataset of product reviews for an E-commerce. 
The goal is to build a sentiment analysis model (this is a sub-field of NLP) that can classify reviews into: Positive or Negative.

Sentiment Analysis Streamlit App



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
When it comes to dealing with classification problems such as this a good metric to look out for is the F1 score of the classes involved. This is because it provides robust results for both balanced and imbalanced dataset unlike accuracy. F1 score is the harmonic mean of precision and recall, which means that the F1 score will tell you the model’s balanced ability to both capture positive cases (recall) and be accurate with the cases it does capture (precision). [Learn More](https://stephenallwright.com/good-f1-score/)

Working with our imbalanced dataset we got an accuracy score of 88% although the accuracy score is really goood, the F-1 score for both classes wasn't really good. The F1 score of the minority class was lower than that of the majority class which showed that our model didn't fully consider the minority class when making predictions.

This is a bias and we can't deploy our model while it makes errors when predicting. To correct this I used the SMOTE technique to solve the issue of imbalance. With this technique our model was able to equally consider both classes when making predictions making the f1 score to greatly improve and it also imporved our accuracy score to 90%.

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
* When saving the model built so it can be incorporated into the streamlit application, I kept getting an error that the size of the model 
has exceeded the github file size limit. I later figured that I needed to incorporate the Github Large File Storage (LFS) so that after saving my model I can easily push my changes to my github repo without any issues. 
### **Resources to learn more about Git LFS**
   - [Learn more about Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage)
   - [Watch this video](https://youtu.be/9HCsSD5PMSk?si=cIaGK9wcmYDp67FT)

* Imbalanced Dataset: Used the SMOTE technique from the imblearn library
[Learn more about SMOTE and other techniques for imbalanced data](https://youtu.be/JnlM4yLFNuo?si=gvGuh9j9em_EVyxa)












[Photo Credit](https://www.bing.com/images/search?view=detailV2&ccid=IcQICE%2ft&id=4B5076CC6F4537E75999D6B878141EB4DC408FD7&thid=OIP.IcQICE_tm9Ksxf_uPT-yAgHaE7&mediaurl=https%3a%2f%2f1.bp.blogspot.com%2f-MVVCz9iyaBw%2fXtNd496XO3I%2fAAAAAAAADBI%2f6fWsE4fLeHw4URtsXNZg3xLZFqjHjeSQQCLcBGAsYHQ%2fs1600%2fama.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.21c408084fed9bd2acc5ffee3d3fb202%3frik%3d149A3LQeFHi41g%26pid%3dImgRaw%26r%3d0&exph=1066&expw=1600&q=amazon+product+reviews+image&simid=608046749928927547&FORM=IRPRST&ck=CF742F167864E3F4FB4B60C8ACA61E97&selectedIndex=0&itb=0&idpp=overlayview&ajaxhist=0&ajaxserp=0)
