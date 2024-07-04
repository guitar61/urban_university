def fake_divide(first_num, second_num):
    try:
        return first_num / second_num
    except ZeroDivisionError:
        return "Error"


if __name__ == '__main__':
    result1 = fake_divide(69, 3)
    result2 = fake_divide(3, 0)
    print(result1)
    print(result2)
