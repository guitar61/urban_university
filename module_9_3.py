first = ['Strings', 'Student', 'Computers']
second = ['String', 'Urban', 'Computer']

first_result = (len(f)-len(s) for f, s in zip(first, second) if len(f) != len(s))
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))