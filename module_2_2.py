first_number = int(input("Please Enter The First Number : "))
second_number = int(input("Please Enter The Second Number : "))
third_number = int(input("Please Enter The Third Number : "))

if first_number == second_number and second_number == third_number:
    print(3)
elif first_number != second_number and second_number != third_number and first_number != third_number:
    print(0)
else:
    print(2)

