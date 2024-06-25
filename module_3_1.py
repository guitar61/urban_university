calls = 0


def string_info(string):
    count_calls()
    lower = string.lower()
    upper = string.upper()
    tup = (len(string), upper, lower)
    return tup


def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    if string_lower in (item.lower() for item in list_to_search):
        return True
    else:
        return False


def count_calls():
    global calls
    calls += 1


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
