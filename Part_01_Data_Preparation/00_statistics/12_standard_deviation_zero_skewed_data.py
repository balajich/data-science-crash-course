'''
Compute standard deviation of a data
'''
import pandas as pd

dataset = pd.read_csv('07_zero_skewed_data.csv')

dataset['salary'].std()
