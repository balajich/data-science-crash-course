'''
Missing data in the data set will be imputed with mode for categorical data
'''

# Import essential libraries

import numpy as np
import pandas as pd

# Read student data set
dataset = pd.read_csv('02_missing_categorical_student_gender_data.csv')

# Independent variables-
X = dataset.iloc[:, 0:2].values

# Dependent variable
y = dataset.iloc[:, 2].values

# Import imputer function
from sklearn.impute import SimpleImputer

# Create SimpleImputer object with mode as strategy
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
# Train the imputer
imputer.fit(X[:, 0:2])
# Apply the change
X[:, 0:2] = imputer.transform(X[:, 0:2])
