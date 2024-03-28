![picture](https://github.com/Odeyiany2/FLiT-Apprenticeship-Data-Science-Projects/blob/main/Project_5%20Churn-Prediction-Model-with-Deployment/customer.png)



# Churn Prediction Model for a Telecommunications Company
The goal of this project is to predict whether a customer is likely to churn and deploying our machine learning 
model for real world use with the help of Heroku. 

Customer churn refers to the percentage of customers who stopped purchasing a business
product or rather service in our case, during a period of time.

This project is about understanding why customers leave a business service and also able to predict which customer will leave the service. 


## Tools
* `Github`: for accessing jupyter notebook for coding (data preprocessing, model training and evaluation) and a repo for documentation.
  
* `Python Libraries`:
  - `Pandas`: for data analysis and manipulation
  - `Seaborn`: for high level data visualizations
  - `Scikit Learn`: for ML algorithms
  - `Imblearn`: for dealing with our imbalanced target variable
  - `Tensorflow` and `Keras`: for deep learning
    
* `Heroku`: a cloud platform that simplifies the deployment process of our model


## Data Insights
The following are some insights discovered from our dataset.
* `Univariate Analysis`:
  - Our target variable which is the customer's churn has a percentage of 26.5% for customers that churned and73.5% for customers that didn't. This shows that we are dealing with a highly imbalanced data set
  - The genders in our dataset are equally distributed; 50% Male and 50% Female.
  - Majority of Customers are not Senior Citizens with the exact percentage been 84% for non senior citizens and 16% for senior citizens
  - Over 3500 of customers have a month to month contract with the company.
  - Majority of customers, above 4500 of them do not have dependents.
  - Over 6000 of customers have phone service.
  - Internet Service Distribution is as follows: 44% use Fiber optic, 34% use DSL, and 22% do not use any internet service.

* `Bivariate Analysis`:
  - There is a positive correlation between the monthly charges variable and the total charges variable. The higher the monthly charge, the higher the total charge.
  - A high monnthly charge leads to a high churn
  - A low total charge leads to a high churn.
  - Customers who use the electric check as a medium of payment are high churners
  - Non-senior citizens are high churners
  - Customers with no tech support or online security are high churners
  - Monthly customers are high churners because they are on no contract.

* **The possibility of churn is affected by three factors: the tenure group of the customer, the monthly charge and the total charge. Higher monthly charge at low tenure leads to low total charge.  Low tenure group, high monthly charge and low total charge results in high churn.** 



## **Problems Encountered and How they were Solved**
* The very first issue encountered which was discovered when Exploratory Data Analysis was conducted, was the issue of imbalanced dataset. Our target variable is highly imbalanced which can prove to be a disadvantage when we build our model. If we leave our dataset without dealing with the imbalance, our model will not most likely not consider the minority class when making predictions. To ensure equal consideration of the two values in our target variable `Churn` we need to ensure that our data is balanced by using either the SMOTE technique or Over-Sampling or Under-Sampling technique. Also when dealing with an imbalanced dataset we can't only take into consideration the accuracy or our model because most times our accuracy can be very high and the predictions made only favours the majority class. We need to look at other metrics such as the precision, recall and F-1 score of each class in our traget variable. 
[Learn More](https://youtu.be/JnlM4yLFNuo?si=gvGuh9j9em_EVyxa)



**Image Source:** [Photo Credit](https://daxg39y63pxwu.cloudfront.net/images/blog/churn-models/Customer_Churn_Prediction_Models_in_Machine_Learning.png)
