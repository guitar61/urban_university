numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime = []

not_prime = []

for num in range(2, len(numbers)+1):
    is_prime = True
    for dividing_number in range(2, num):
        if num % dividing_number == 0:
            is_prime = False

    if is_prime:
        prime.append(num)
    else:
        not_prime.append(num)

print(prime)
print(not_prime)



