def print_params(a=1, b='string', c=True):
    return a, b, c


print(print_params(b=25))
print(print_params(c=[1, 2, 3]))
print(print_params())

values_list = [False, 23, "help"]

values_dict = {'a': 'Alex',
               'b': 38,
               'c': 'male'
               }
print(print_params(*values_list))
print(print_params(**values_dict))

values_list_2 = [None, 34]

print(print_params(*values_list_2, 42))

