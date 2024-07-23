class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Create a new instance of the class
        instance = super(House, cls).__new__(cls)
        # Add the name of the house to the houses_history list
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name: str, num_of_floors: int):
        self.name = name
        self.num_of_floors = num_of_floors

    def __del__(self):
        print(f"{self.name} has been demolished, but it will remain in history")

    def go_to(self, new_floor: int) -> None:
        if new_floor > self.num_of_floors or new_floor < 1:
            print('"There is no such floor"')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self) -> int:
        return self.num_of_floors

    def __str__(self) -> str:
        return f"Name: {self.name}, Number of floors: {self.num_of_floors}"

    def __eq__(self, other) -> bool:
        if isinstance(other, House):
            return self.num_of_floors == other.num_of_floors
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, House):
            return self.num_of_floors < other.num_of_floors
        return False

    def __gt__(self, other) -> bool:
        if isinstance(other, House):
            return self.num_of_floors > other.num_of_floors
        return False

    def __le__(self, other) -> bool:
        if isinstance(other, House):
            return self.num_of_floors <= other.num_of_floors
        return False

    def __ge__(self, other) -> bool:
        if isinstance(other, House):
            return self.num_of_floors >= other.num_of_floors
        return False

    def __ne__(self, other) -> bool:
        if isinstance(other, House):
            return self.num_of_floors != other.num_of_floors
        return False

    def __add__(self, value: int) -> 'House':
        if isinstance(value, int):
            return House(self.name, self.num_of_floors + value)
        return NotImplemented

    def __radd__(self, value: int) -> 'House':
        return self.__add__(value)

    def __iadd__(self, value: int) -> 'House':
        if isinstance(value, int):
            self.num_of_floors += value
            return self
        return NotImplemented


# # Testing the implementation
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
#
# print(h1 == h2)  # __eq__
#
# h1 = h1 + 10  # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10  # __iadd__
# print(h1)
#
# h2 = 10 + h2  # __radd__
# print(h2)
#
# print(h1 > h2)  # __gt__
# print(h1 >= h2)  # __ge__
# print(h1 < h2)  # __lt__
# print(h1 <= h2)  # __le__
# print(h1 != h2)  # __ne__


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
