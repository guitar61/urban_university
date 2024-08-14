def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item
        except TypeError:
            print(f"Invalid data type for calculating sum - {item}")
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        if len(numbers) == 0 or (len(numbers) == incorrect_data):
            return 0
        return total_sum / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("Incorrect data type written to numbers")
        return None


# Example usage
print(f'Result 1: {calculate_average("1, 2, 3")}')  # The string is iterated over, but each character is a string
print(f'Result 2: {calculate_average([1, "String", 3, "Another String"])}')  # Only 1 and 3 are taken into account
print(f'Result 3: {calculate_average(567)}')  # A non-collection was passed
print(f'Result 4: {calculate_average([42, 15, 36, 13])}')  # Everything should work
