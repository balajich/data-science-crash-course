# Import essential libraries
import pandas as pd

# read data file
dataset = pd.read_csv('16_assignment_employee_annual_salary.csv');
# Mean
dataset['AnnualSalaryInUSD'].mean()  # Answer 189893.63
# Median
dataset['AnnualSalaryInUSD'].median()  # Median 54330

from scipy import stats

# Mode
stats.mode(dataset['AnnualSalaryInUSD']) # Mode 54000
