immutable_var = 1, 2, 4, 5, True, "name", "age"

print(immutable_var)

try:
    immutable_var[0] = 3
except TypeError:
    print ("Tuples are immutable, cannot modify elements")

'''The tuple collection 's element can not be changed or modified after being assigned '''

mutable_list = [1, 2, 4, 5, [True, "name", "age"]]

mutable_list[0] = 0
mutable_list[1] = 1
mutable_list[2] = 2
mutable_list[3] = 10
mutable_list[4][0] = False
mutable_list[4][2] = "gender"

print(mutable_list)


