# import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data Extraction - Reading dataset from csv file
dataset = pd.read_csv('00_first_model_data.csv', header=None)

# Create independent variable
X = dataset.iloc[:, 0].values

# Create dependent variable
y = dataset.iloc[:, 1].values

# Visualize the data
plt.scatter(X, y)

# Split data into train and test set
# Using machine learning SKLearn Library
from sklearn.model_selection import train_test_split

# Split data into 80 (train) to 20 (test) ratio
# Random state is taken as zero. So that all of us get same test and train data sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=0)

# Create Linear Regressor
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

# Train model using train data set
regressor.fit(X_train.reshape(-1, 1), y_train)

# Predict using test data set
y_pred = regressor.predict(X_test.reshape(-1, 1))

# Predict on new data set. Example user gave value 14 to X
y_pred_new = regressor.predict(np.array([14]).reshape(-1, 1))

