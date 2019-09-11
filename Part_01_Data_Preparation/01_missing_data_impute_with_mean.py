'''
Missing data in the data set will be imputed with mean
'''

# Import essential libraries

import pandas as pd

# Read car purchase dataset
dataset = pd.read_csv('00_car_purchase_data.csv')

# Independent variables
X = dataset.iloc[:, 0:3].values

# Dependent variable
y = dataset.iloc[:, 3].values

# Import imputer function
from sklearn.preprocessing import Imputer

# Create imputer object with mean as strategy and to use values in columns
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
# Train the imputer
imputer.fit(X[:, 1:3])
# Apply the change
X[:, 1:3] = imputer.transform(X[:, 1:3])
