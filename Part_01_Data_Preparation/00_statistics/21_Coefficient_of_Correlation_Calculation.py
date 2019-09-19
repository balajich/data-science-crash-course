'''
Identify correlation between variables
'''

# Import essential libraries
import pandas as pd

# Read data set
dataset = pd.read_csv('20_Coefficient_of_Correlation_Cigraettes_Smoked_per_week.csv')

# Draw scatter plot identify correlation
dataset.plot.scatter(x='CigratesSmokedPerWeek', y='NumberOfYearsLived',
                     title='CigratesSmokedPerWeek vs NumberOfYearsLived', color='c')

# Calculate Pearson correlation coefficient
from scipy.stats import pearsonr

r, _ = pearsonr(dataset['CigratesSmokedPerWeek'], dataset['NumberOfYearsLived'])  # Answer is -0.61
