first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
combined_list = first_strings + second_strings

first_result = [len(string) for string in first_strings if len(string) >= 5]
second_result = [(name, n)for name in first_strings for n in second_strings if len(name) == len(n)]
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)