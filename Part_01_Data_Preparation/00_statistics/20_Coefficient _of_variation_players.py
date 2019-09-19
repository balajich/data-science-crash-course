'''Calculate Coefficient of variation'''

# import libraries
import pandas as pd

# Read dataset
dataset = pd.read_csv('19_coefficient_of_variation_players_data.csv')
player_a_mean = dataset['PlayerA'].mean()  # Answer 49.8
player_a_sd = dataset['PlayerA'].std()  # Answer 44.57
# Player A Coefficient of variation
payer_a_cv = player_a_sd / player_a_mean # 0.89


player_b_mean = dataset['PlayerB'].mean()  # Answer 32.7
player_b_sd = dataset['PlayerB'].std()  # Answer 24.43
# Player B Coefficient of variation
payer_b_cv = player_b_sd / player_b_mean # 0.747
