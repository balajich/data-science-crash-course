'''
Compute Mode pizza cost per resutrant in City
Modes are impacted by outliers
'''
# import essential libraries
import pandas as pd

dataset = pd.read_csv('00_pizza_cost_per_city_in_India.csv')
# Mode pizza cost in Hyderabad
dataset['Pizza Cost Hyderabad in Dollars'].mode()

# Mode pizza cost in Mumbai:
dataset['Pizza Cost Mumbai in Dollars'].mode()
