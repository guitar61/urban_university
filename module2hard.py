import random

# generating a random number between 3 - 20
n = random.randint(3, 20)
print(f"{n} : is the random number selected.\n")

mylist = []
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            mylist.append(i)
            mylist.append(j)

# all the possible password for the random number generated
for i in mylist:
    print(f"{i}", end=" ")
