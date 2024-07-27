class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'white', 'black']

    def __init__(self, owner, model, color, engine):
        self.owner = owner
        self.__model = model
        self.__engine = engine
        self.__color = color

    def get_model(self):
        return f"Model: {self.__model}"

    def get_horsepower(self):
        return f"Engine power: {self.__engine}"

    def get_color(self):
        if self.__color.lower() == 'black':
            return f"Color: BLACK"
        else:
            return f"Color: {self.__color.lower()}"

    def print_info(self):
        print(f"{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nOwner: {self.owner}")

    def set_color(self, new_color: str):
        new_color_lower = new_color.lower()
        if new_color_lower in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Cannot change color to {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Current colors __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Initial properties
vehicle1.print_info()

# Changing properties (including calling methods)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Checking what has changed
vehicle1.print_info()
