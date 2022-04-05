import numpy as np
import pandas as pd


def print_value(value):
    value_name = [name for name in globals() if globals()[name] is value]
    print(f'= {value_name}: {value}')


# TASK 01

data_np = np.genfromtxt('Zadanie_1.csv', delimiter=';', skip_header=1)

print('\n=== TASK 1 ===')
number_of_cells = np.count_nonzero(data_np)
shape = data_np.shape
mean = np.nanmean(data_np)
median = np.nanmedian(data_np)
variance = np.nanvar(data_np)

del_columns_shape = data_np[:, ~np.isnan(data_np).any(axis=0)].shape
del_rows_shape = data_np[~np.isnan(data_np).any(axis=1)].shape

print_value(number_of_cells)
print_value(shape)
print_value(mean)
print_value(median)
print_value(variance)

print_value(del_columns_shape)
print_value(del_rows_shape)

# TASK 02

data_two_np = np.genfromtxt('Zadanie_2.csv', delimiter=';')

print('\n=== TASK 2 ===')
values, vectors = np.linalg.eig(data_two_np)
inverse_matrix = np.linalg.inv(data_two_np)

print_value(values)
print_value(vectors)
print_value(inverse_matrix)

# TASK 03

data_31_np = np.genfromtxt('Zadanie_3_macierz_A.csv', delimiter=',')
data_32_np = np.genfromtxt('Zadanie_3_macierz_B.csv', delimiter=',')

print('\n=== TASK 3 ===')
up = np.dot(data_31_np, data_32_np.transpose())
down = np.sqrt(np.sum(data_31_np**2, axis=1))[:, np.newaxis] * np.sqrt(
    np.sum(data_32_np**2, axis=1))[np.newaxis, :]
cos_sim = up / down

print_value(cos_sim)

# TASK 4

data_4_pd = pd.read_csv('Zadanie_4.csv', sep=';')
data_4_pd = data_4_pd.dropna(axis=1, how='all')

print('\n=== TASK 4 ===')

data_4_pd['DateTime'] = pd.to_datetime(data_4_pd['DateTime'],
                                       format='%d.%m.%Y %H:%M')

data_4_pd = data_4_pd.groupby(['DoctorID'])

by_doctor = data_4_pd.groups.keys()
list_min = list(data_4_pd['DateTime'].min())
list_max = list(data_4_pd['DateTime'].max())
city = list(data_4_pd['City'].first())
doc_type = list(data_4_pd['Type'].first())

new_df = pd.DataFrame({
    "TimeStart": list_min,
    "TimeEnd": list_max,
    "DoctorID": by_doctor,
    'Type': doc_type,
    'City': city
})

print(new_df)

new_df.to_csv('Zadanie_4_odp.csv', index=False)
