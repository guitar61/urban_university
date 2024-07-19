class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors
        House.houses_history.append(self.name)

    def __del__(self):
        print(f"{self.name} has been demolished, but it will remain in history")

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

    def __eq__(self, other):
        if isinstance(other, House):
            return self.num_of_floors == other.num_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors < other.num_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.num_of_floors <= other.num_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors > other.num_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.num_of_floors >= other.num_of_floors
            return True

    def __ne__(self, other):
        if isinstance(other, House):
            return self.num_of_floors != other.num_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.num_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('Residential Complex Elbrus', 10)
print(House.houses_history)
h2 = House('Residential Complex Acacia', 20)
print(House.houses_history)
h3 = House('Residential Complex Matryoshka', 20)
print(House.houses_history)

# Deleting objects
del h2
del h3

print(House.houses_history)
