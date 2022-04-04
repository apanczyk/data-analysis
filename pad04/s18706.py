from cmath import isnan
from operator import delitem
from unittest import skip
import numpy as np
import pandas as pd
import numpy as np

# TASK 01

data_np = np.genfromtxt('Zadanie_1.csv', delimiter=';', skip_header=1)

print(np.count_nonzero(data_np))
print(data_np.shape)

print(np.nanmean(data_np))
print(np.nanmedian(data_np))    
print(np.nanvar(data_np))


data_np_del_columns = data_np[:, ~np.isnan(data_np).any(axis=0)]
data_np_del_rows = data_np[~np.isnan(data_np).any(axis=1)]

print(data_np_del_columns.shape)
print(data_np_del_rows.shape)
