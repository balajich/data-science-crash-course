'''
Compute mean pizza cost per resutrant in City
Mean is impacted by outlier
'''
# import essential libraries
import pandas as pd

dataset = pd.read_csv('00_pizza_cost_per_city_in_India.csv')
# Mean pizza cost in Hyderabad
dataset['Pizza Cost Hyderabad in Dollars'].mean()

# Mean pizza cost in Mumbai:
dataset['Pizza Cost Mumbai in Dollars'].mean()
