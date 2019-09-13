'''
Compute Median pizza cost per resutrant in City
'''
# Calculate median using pandas
# import essential libraries
import pandas as pd

dataset = pd.read_csv('00_pizza_cost_per_city_in_India.csv')
# Median pizza cost in Hyderabad
dataset['Pizza Cost Hyderabad in Dollars'].median()

# Median pizza cost in Mumbai:
dataset['Pizza Cost Mumbai in Dollars'].median()

# Calculate median using numpy
import numpy as np

np.median(np.array([1, 2, 3, 4, 5]))  # 3 is answer
np.median(np.array([1, 2, 3, 4, 5, 6]))  # 3.5 is answer(i.e) mean of 3 and 4  is answer
