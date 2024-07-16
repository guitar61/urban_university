class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to(self, new_floor):
        if new_floor > self.num_of_floors or new_floor < 1:
            print("This floor does not exist")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

# Example usage
h1 = House('ZhK Gorskiy', 18)
h2 = House('Domik v derevne', 2)

h1.go_to(5)  # Expected output: 1, 2, 3, 4, 5
h2.go_to(10)  # Expected output: "This floor does not exist"


