'''Calcuate variance and standard deviation of employee annual salaries '''

# import essential libraries

import pandas as pd

# Read data set
dataset = pd.read_csv('16_assignment_employee_annual_salary.csv')

# calculate standard deviation
dataset['AnnualSalaryInUSD'].std()  # Answer 365269

# Variance
dataset['AnnualSalaryInUSD'].std() ** 2 # Answer 133422147445
