'''
Analyze the salary distribution of employees in a company
In positive skewed mean is greater than median
'''
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('05_postively_skewed_data.csv')

dataset['salary'].mean() # Mean 27894.73
dataset['salary'].median() # Median 20000
from scipy import stats

stats.mode(dataset['salary'])# Mode 20000
plt.hist(dataset['salary'],bins=5)
