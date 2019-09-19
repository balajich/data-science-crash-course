'''
Analyze the distribution of data
In Zero skewed mean=median=mode
'''
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('07_zero_skewed_data.csv')

dataset['salary'].mean()  # Mean 40000
dataset['salary'].median()  # Median 40000
from scipy import stats

stats.mode(dataset['salary'])  # Mode 40000
# visualization
# Histogram of Salary
dataset['salary'].plot(kind='hist', title='Histogram for Salary', color='c')
# use kde for density plot
dataset['salary'].plot(kind='kde', title='Density plot for Salary', color='c')

# import essential libraries
import numpy as np

# Employee Salaries
np_array = np.array(
    [10000, 10000, 20000, 20000, 30000, 30000, 30000, 40000, 40000, 40000, 40000, 40000, 50000, 50000, 50000, 60000,
     60000, 70000, 70000])
np.mean(np_array)
np.median(np_array)

from scipy import stats

stats.mode(np_array)  # Mode 40000
plt.hist(np_array, bins=5)

