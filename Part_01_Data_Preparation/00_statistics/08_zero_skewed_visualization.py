'''
Analyze the distribution of data
In Zero skewed mean=median=mode
'''
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('07_zero_skewed_data.csv')

dataset['salary'].mean() # Mean 40000
dataset['salary'].median() # Median 40000
from scipy import stats

stats.mode(dataset['salary'])# Mode 40000
plt.hist(dataset['salary'],bins=5)
