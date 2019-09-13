'''
Compute Median pizza cost per resutrant in City
'''
# import essential libraries
import pandas as pd

dataset = pd.read_csv('00_pizza_cost_per_city_in_India.csv')
# Median pizza cost in Hyderabad
dataset['Pizza Cost Hyderabad in Dollars'].median()

# Median pizza cost in Mumbai:
dataset['Pizza Cost Mumbai in Dollars'].median()
