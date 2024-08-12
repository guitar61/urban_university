def add_everything_up(x, y):
    try:
        return round(x + y, 3)
    except TypeError:
        return str(x) + str(y)



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))