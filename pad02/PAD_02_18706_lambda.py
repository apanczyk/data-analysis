# TASK 1
print("# TASK 1")

sum15 = lambda var: var + 15
multiply = lambda x, y: x * y

sum = sum15(10)
multiply = multiply(6, 7)
print(sum)
print(multiply)

# TASK 2
print("# TASK 2")

list_with_dict = [{
    'make': 'Nokia',
    'model': 216,
    'color': 'Black'
}, {
    'make': 'Mi Max',
    'model': 2,
    'color': 'Gold'
}, {
    'make': 'Samsung',
    'model': 7,
    'color': 'Blue'
}]

sort_list = lambda sort_by: sorted(list_with_dict,
                                   key=lambda key: key[sort_by])
sorted_by_model = sort_list('model')
sorted_by_color = sort_list('color')
print(sorted_by_model)
print(sorted_by_color)

# TASK 3
print("# TASK 3")

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pow_n_list = lambda n_list, pow: tuple(map(lambda x: x**pow, n_list))

pow_2_list = pow_n_list(number_list, 2)
pow_3_list = pow_n_list(number_list, 3)
print(pow_2_list)
print(pow_3_list)
