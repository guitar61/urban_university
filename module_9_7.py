def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            print("Составное")
            return result
        for num in range(2, int(result ** 0.5) + 1):
            if result % num == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper


@is_prime
def sum_three(n1, n2, n3):
    total = n1 + n2 + n3
    return total


result = sum_three(2, 3, 6)
print(result)
