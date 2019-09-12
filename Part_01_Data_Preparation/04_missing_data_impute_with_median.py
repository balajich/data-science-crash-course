'''
Missing data in the data set will be imputed with median because data has outlier.
'''

# Import essential libraries

import pandas as pd
import numpy as np

# Read car purchase dataset
dataset = pd.read_csv('04_missing_data_employee_salary.csv')

# Independent variables
X = dataset.iloc[:, 0:2].values

# Dependent variable
y = dataset.iloc[:, 2].values

# Import imputer function
from sklearn.impute import SimpleImputer

# Create SimpleImputer object with median as strategy to use
imputer = SimpleImputer(missing_values=np.nan, strategy='median')
# Train the imputer
imputer.fit(X[:, 0:2])
# Apply the change
X[:, 0:2] = imputer.transform(X[:, 0:2])
