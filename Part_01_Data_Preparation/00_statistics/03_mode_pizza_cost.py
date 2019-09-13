'''
Compute Mode pizza cost per resutrant in City
Modes are impacted by outliers
'''
# Calculate mode using pandas
# import essential libraries
import pandas as pd

dataset = pd.read_csv('00_pizza_cost_per_city_in_India.csv')
# Mode pizza cost in Hyderabad
dataset['Pizza Cost Hyderabad in Dollars'].mode()

# Mode pizza cost in Mumbai:
dataset['Pizza Cost Mumbai in Dollars'].mode()

# Calcuate mode using numpy and scipy
import numpy as np
from scipy import stats

np_array = np.array([1, 2, 3, 3, 4, 5])
stats.mode(np_array)  # Answer is 3
