'''
Mean and mode are impacted by outliers
Where as median is not
'''
import numpy as np

np_array = [1, 2, 3, 4, 5, 6, 100, 100]
np.mean(np_array)  # Answer is 27.65
np.median(np_array)  # Answer is 4.5

from scipy import stats

stats.mode(np_array)  # Answer is 100
