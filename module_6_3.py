class Horse:
    def __init__(self, x_distance=0, sound='Frrr'):
        super().__init__()
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        super().__init__()
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance=0, y_distance=0):
        super().__init__(x_distance=x_distance, sound='Frrr')
        self.y_distance = y_distance
        self.sound = 'I train, eat, sleep, and repeat'

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


# Create an instance of Pegasus and test the methods
p1 = Pegasus()

print(p1.get_pos())  # Should print (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # Should print (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # Should print (5, 35)
p1.voice()  # Should print 'I train, eat, sleep, and repeat'
