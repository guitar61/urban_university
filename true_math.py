from math import inf


def true_divide(first_num, second_num):
    if second_num == 0:
        return inf
    else:
        return first_num / second_num


if __name__ == '__main__':
    result3 = true_divide(49, 7)
    result4 = true_divide(15, 0)
    print(result3)
    print(result4)
