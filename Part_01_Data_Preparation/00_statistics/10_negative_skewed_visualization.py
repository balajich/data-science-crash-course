'''
Analyze the distribution of data
In negative skewed mean is less than median and mode
'''
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('09_negative_skewed_data.csv')

dataset['salary'].mean() # Mean 49000
dataset['salary'].median() # Median 50000
from scipy import stats

stats.mode(dataset['salary'])# Mode 60000

# visualization
# Histogram of Salary
dataset['salary'].plot(kind='hist', title='Histogram for Salary of negatively skewed data', color='c', bins=10)
# using kde for density plot
dataset['salary'].plot(kind='kde', title='Density plot for Salary of negatively skewed data', color='c')

