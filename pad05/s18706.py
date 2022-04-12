from ntpath import join
import string
import numpy as np
import pandas as pd

# TASK 1

orders = pd.read_csv('orders.csv')

# TASK 1a
orders['order_date'] = pd.to_datetime(orders['order_date'], format='%Y-%m-%d')
print(orders['order_date'])

# TASK 1b
unique = orders['tshirt_category'].unique()
print(unique)
print(unique.size)

# TASK 1c
replace = lambda old, new: orders['tshirt_category'].apply(lambda x: x.replace(
    old, new))

orders['tshirt_category'] = replace('Wh ', 'White ')
orders['tshirt_category'] = replace('Bl ', 'Black ')
orders['tshirt_category'] = replace('Tshirt ', 'T-Shirt ')

unique = orders['tshirt_category'].unique()
print(unique)
print(unique.size)

# TASK 1d
split = lambda regex, num: orders['tshirt_category'].apply(lambda x: x.split(
    regex)[num])

orders['tshirt_category'] = replace('Hoodie', ' Hoodie ')
orders['tshirt_category'] = replace('Tennis Shirt', ' Tennis,Shirt ')

orders['tshirt_type'] = split(" ", 1)
orders['tshirt_color'] = split(" ", 0)
orders['tshirt_size'] = split(" ", 2)
print(orders)

# TASK 1e
filtered_orders = orders.loc[orders['order_date'].between(
    '2014-12-31', '2016-08-02')]
print(filtered_orders)

# TASK 2

customers = pd.read_csv('customers.csv')

# TASK 2a

print(customers.columns)

# TASK 2b

print(f'{customers.shape} {orders.shape}')

# TASK 2c

customers.rename(columns={'customerID': 'customer_id'}, inplace=True)
print(customers.columns)

# TASK 2d

# Join, ponieważ jeden customer może mieć wiele zamówień

joined = orders.set_index('customer_id').join(
    customers.set_index('customer_id'))
print(joined)

# TASK 3

joined.to_csv("joineds18706.csv", index=False)
