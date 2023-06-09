# -*- coding: utf-8 -*-
"""PCA_RA2011030010214.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-jsLrh-lZZKHLSBamt-83uhPll6c_ZRb
"""

# Importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report

# Loading the dataset
iris = load_iris()

# Converting the dataset to a Pandas dataframe
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Adding the target variable to the dataframe
iris_df['target'] = iris.target

"""In this first section of the code, we import the necessary libraries and load the Iris dataset. We then convert the dataset to a Pandas dataframe and add the target variable to the dataframe."""

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris_df.drop('target',axis=1), 
                                                    iris_df['target'], test_size=0.30, 
                                                    random_state=101)

# Scaling the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Fitting the logistic regression model
model = LogisticRegression()
model.fit(X_train,y_train)

# Predicting on the test set
predictions = model.predict(X_test)

# Printing the classification report
print(classification_report(y_test,predictions))

"""In this next section of the code, we split the dataset into training and testing sets and scale the data using StandardScaler(). We then fit a logistic regression model to the training data and make predictions on the testing data. Finally, we print the classification report, which shows the precision, recall, and F1 score for each class, as well as the overall accuracy of the model."""

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris_df.drop('target',axis=1), 
                                                    iris_df['target'], test_size=0.30, 
                                                    random_state=101)

# Scaling the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Applying PCA
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Fitting the logistic regression model
model_pca = LogisticRegression()
model_pca.fit(X_train_pca,y_train)

# Predicting on the test set
predictions_pca = model_pca.predict(X_test_pca)

# Printing the classification report
print(classification_report(y_test,predictions_pca))

"""In this final section of the code, we apply Principal Component Analysis (PCA) to the data using PCA() from scikit-learn. We then fit a logistic regression model to the transformed training data and make predictions on the transformed testing data. Finally, we print the classification report for this model, which shows how the performance differs from the model built without PCA.

Overall, this code demonstrates how to build and compare two logistic regression models, one without applying PCA and one after applying PCA, using the popular Iris dataset.
"""