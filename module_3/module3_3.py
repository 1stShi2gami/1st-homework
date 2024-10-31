def print_params(a=1, b='', c=True):
    print(a, b, c)


values_list = [32, 'str', True]
values_dict = {'a': 3, 'b': 'str', 'c': True}
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Hello']
print_params(*values_list_2, 42)