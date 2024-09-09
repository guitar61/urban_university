class Figure:
    sides_count = 0  # Default for all figures

    def __init__(self, sides, color=(0, 0, 0)):
        self.__sides = list(sides)  # Encapsulated list of sides
        self.__color = list(color)  # Encapsulated color in RGB
        self.filled = True  # Public attribute, whether the figure is filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if not self.__is_valid_sides(*new_sides):
            return False
        self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1  # A circle only has one side, the circumference

    def __init__(self, color=(0, 0, 0), circumference=1):
        super().__init__([circumference], color)  # Initialize the parent class
        self.circumference = circumference
        self.radius = circumference / (2 * 3.14159)  # Calculate the radius from the circumference

    def get_square(self):
        return 3.14159 * (self.radius ** 2)  # Area = πr²


class Triangle(Figure):
    sides_count = 3  # A triangle has 3 sides

    def __init__(self, color=(0, 0, 0), side1=1, side2=1, side3=1):
        super().__init__([side1, side2, side3], color)

    def get_square(self):
        a, b, c = self.get_sides()  # Get the three sides
        s = (a + b + c) / 2  # Calculate the semi-perimeter
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Calculate the area using Heron's formula


class Cube(Figure):
    sides_count = 12  # A cube has 12 edges

    def __init__(self, color=(0, 0, 0), edge=1):
        super().__init__([edge] * 12, color)  # Pass 12 identical edges to the parent class

    def get_volume(self):
        edge = self.get_sides()[0]  # All edges of the cube are the same
        return edge ** 3  # Volume = edge³


circle1 = Circle((200, 200, 100), 10) # (Color, sides)
cube1 = Cube((222, 35, 130), 6)

# Check for color change:
circle1.set_color(55, 66, 77) # Will change
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Will not change
print(cube1.get_color())

# Check for side change:
cube1.set_sides(5, 3, 12, 4, 5) # Will not change
print(cube1.get_sides())
circle1.set_sides(15) # Will change
print(circle1.get_sides())

# Check perimeter (of circle), this is length:
print(len(circle1))

# Check volume (of cube):
print(cube1.get_volume())
