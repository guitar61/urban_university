my_dict = {'name'.title(): 'alex'.title(),
           'phone number'.title(): '09143010466',
           'country'.title(): 'Turkey',
           'city'.title(): 'istanbul'.title(),
           'birthday'.title(): 1982,
           }

print(my_dict)

print(my_dict['country'.title()])

print(my_dict.get('skin color', 'this key is not found on the dic'))

my_dict.update({'country'.title(): 'iran'.title(),
                'age'.title(): 29, })

print(my_dict)

removed_value = my_dict.pop('age'.title())

print(removed_value)

print(my_dict)

my_set = {0, 1, 1, 2, 3, 4, 3, 'ali', 'reza', 'ali', True, True, False}

print(my_set)

my_set.update({10, 'mohammad'})

print(my_set)

my_set.pop()

print(my_set)
