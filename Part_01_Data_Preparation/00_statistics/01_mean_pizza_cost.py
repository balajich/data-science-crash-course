'''
Compute mean pizza cost per resutrant in City
Mean is impacted by outlier
'''
# import essential libraries
import pandas as pd

# Calculate mean using pandas
dataset = pd.read_csv('00_pizza_cost_per_city_in_India.csv')
# Mean pizza cost in Hyderabad
dataset['Pizza Cost Hyderabad in Dollars'].mean()

# Mean pizza cost in Mumbai:
dataset['Pizza Cost Mumbai in Dollars'].mean()

# Calculate mean using numpy
import numpy as np

np_array = np.array([1, 2, 3, 4, 5])
np.mean(np_array) # answer is 3.0
