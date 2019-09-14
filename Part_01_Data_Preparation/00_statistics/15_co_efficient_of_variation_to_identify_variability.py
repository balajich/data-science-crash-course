'''
Compute Coefficient of variation
'''
import pandas as pd

dataset = pd.read_csv('14_employee_salary_india_usa_data.csv')

usa_coefficient_of_variation = dataset['USA'].std() / dataset['USA'].mean()
india_coefficient_of_variation = dataset['INDIA'].std() / dataset['INDIA'].mean()
