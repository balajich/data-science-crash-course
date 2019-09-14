'''
Compute Coefficient of variation
'''
import pandas as pd

dataset = pd.read_csv('07_zero_skewed_data.csv')

dataset['salary'].std() / dataset['salary'].mean()
