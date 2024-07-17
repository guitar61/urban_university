class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f"Name: {self.name}, number of floors: {self.num_of_floors}"

    def go_to(self, new_floor):
        if new_floor > self.num_of_floors or new_floor < 1:
            print("This floor does not exist")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


# Example usage
h1 = House('Elbrus Apartment', 10)
h2 = House('Acacia Apartment', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
