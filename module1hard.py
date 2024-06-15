grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

average_list = []

for sub_list in grades:
    avg = sum(sub_list) / len(sub_list)
    average_list.append(avg)

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_list = sorted(students)

student_dic = {}

for name, average in zip(sorted_list, average_list):
    student_dic[name] = average

print(student_dic)
