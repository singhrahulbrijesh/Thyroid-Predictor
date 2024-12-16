## **Thyroid-Detection using Machine Learning techniques**

## Problem Statement
Thyroid disease is a widespread health issue in India, affecting over 10 million people annually. This condition can disrupt the body's metabolism, either speeding it up or slowing it down. This project aimed to develop a tool that could help identify different types of thyroid disorders.

## How the Project Works
We used machine learning to build a model that can predict whether a person has compensated hypothyroidism, primary hypothyroidism, secondary hypothyroidism, or no thyroid disorder at all. To do this, we trained the model on a large dataset of patient information from the UCI Machine Learning Repository.

We experimented with several machine-learning algorithms, including **Random Forest**, **XGBoost**, and **KNN**. After fine-tuning these algorithms, we found that XGBoost performed the best, achieving high accuracy, precision, and recall.

## Real-World Application

To make this model accessible to people, we deployed it as a web application using the Flask framework and hosted it on Heroku. This means that anyone can use the application to input their medical information and receive a prediction about their thyroid health.

In essence, this project aims to provide a valuable tool for early detection and diagnosis of thyroid disorders in India, potentially improving the lives of millions of people.

## Streamlit link - If the below link is not working, the free trial period may have ended. However, you can see the video below :)
Streamlit:- https://thyroid-predictor.streamlit.app/


## Image of the Project
![Thyroid prediction image ](https://github.com/user-attachments/assets/3928cb1d-f5aa-4001-933f-94372330a27c)
[Watch the video] - 

https://github.com/user-attachments/assets/b33a832d-1d48-46f5-97b5-fc07ce6754f5


## Architecture
![](https://github.com/singhrahulbrijesh/Thyroid-Detection-main/blob/master/Thyroid-Detection-main/Images/architecture.jpg)

<a href="https://drive.google.com/uc?export=view&id=1Pg1EQG6dGE-rC7-ug9k-QXnaSvrGRAZ1"><img src="https://drive.google.com/uc?export=view&id=1Pg1EQG6dGE-rC7-ug9k-QXnaSvrGRAZ1" style="width: 100px; max-width: 50%; height: auto" title="Click for the larger version." /></a>
<a href="https://drive.google.com/uc?export=view&id=1Pc8kV7yDDvvv5VE9h4DJhTliiTtpJSfj"><img src="https://drive.google.com/uc?export=view&id=1Pc8kV7yDDvvv5VE9h4DJhTliiTtpJSfj" style="width: 100px; max-width: 50%; height: auto" title="Click for the larger version." /></a>


## Data Description
The client will send data in multiple sets of files in batches at a given location. Data will contain different classes of thyroid and 30 columns of different values.
"Class" column will have four unique values “negative, compensated_hypothyroid,
primary_hypothyroid, secondary_hypothyroid”.
Apart from training files, we also require a "schema" file from the client, which contains all the relevant information about the training files such as:
Name of the files, Length of Date value in FileName, Length of Time value in FileName, Number of Columns, Name of the Columns, and their datatype.

## Data Validation 
In this step, we perform different sets of validation on the given set of training files.  
1.	 Name Validation
2.	 Number of Columns
3.	 Name of Columns
4.	 The datatype of columns
5.	 Null values in columns

## Data Insertion in Database 
1) Database Creation and connection - Create a database with the given name passed. If the database is already created, open the connection to the database. 
2) Table creation in the database - Table with name 
3) Insertion of files in the table

## Model Training 
1) Data Export from Db
2) Data Preprocessing   
   a) Drop columns not useful for training the model. Such columns were selected while doing the EDA.
   b) Replace the invalid values with numpy “nan” so we can use imputer on such values.
   c) Encode the categorical values
   d) Check for null values in the columns. If present, impute the null values using the KNN imputer.
   e)  After imputing, handle the imbalanced dataset by using RandomOverSampler.
3) Clustering - The KMeans algorithm creates clusters in the preprocessed data. The optimum number of clusters is selected by plotting the elbow plot, and for the dynamic selection of the number of clusters, we are using the "KneeLocator" function. The idea behind clustering is to implement different algorithms
   To train data in different clusters, the K-means model is trained over preprocessed data and saved for further use in prediction.
4) Model Selection—After clusters are created, we find the best model for each cluster. We use two algorithms, "Random Forest" and "KNN." For each cluster, both algorithms are passed with the best parameters derived from GridSearch. We calculate the AUC scores for both models and select the model with the best score. Similarly, the model is selected for each cluster. All the models for every cluster are saved for use in prediction. 

## Prediction Data Description 
The client will send the data in multiple sets of files in batches at a given location. Apart from prediction files, we also require a "schema" file from the client which contains all the relevant information about the training files such as the name of the files, Length of Date value in FileName, Length of Time value in FileName, Number of Columns, Name of the Columns and their datatype.

## Data Validation - For Prediction Data
In this step, we perform different sets of validation on the given set of training files.  
1.	 Name Validation
2.	 Number of Columns
3.	 Name of Columns
4.	 The datatype of columns
5.	 Null values in columns

## Data Insertion in Database - For Prediction Data
1) Database Creation and connection - Create a database with the given name passed. If the database is already created, open the connection to the database. 
2) Table creation in the database - Table with name 
3) Insertion of files in the table

## Prediction 
 
1) Data Export from Db
2) Data Preprocessing   
   a) Drop columns are not useful for training the model. Such columns were selected while doing the EDA.
   b) Replace the invalid values with numpy “nan” so we can use imputer on such values.
   c) Encode the categorical values
   d) Check for null values in the columns. If present, impute the null values using the KNN imputer.
3) Clustering - The KMeans model created during training is loaded, and clusters for the preprocessed prediction data is predicted.
4) Prediction - Based on the cluster number, the respective model is loaded and is used to predict the data for that cluster.
5) Once the prediction is made for all the clusters, the predictions along with the original names before label encoder are saved in a CSV file at a given location and the location is returned to the client.

## Deployment
We can deploy to Cloud Based Service Platforms for example Heroku or AWS, GCP, AZURE. 
This is a workflow diagram for the prediction of using the trained model.   


Result: - 
Designed a scalable end-to-end machine learning pipeline utilizing clustering and classification techniques to accurately determine compensation for hypothyroidism in patients and the AUC score of 0.9%.
Achieved an impressive accuracy of 94.5%, ensuring reliable and accurate predictions for patient diagnosis.



