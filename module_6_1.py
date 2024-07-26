class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.alive = alive
        self.fed = fed
        self.name = name


class Plant:
    def __init__(self, name, edible=False):
        self.edible = edible
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} ate {food.name}")
                self.fed = True
            else:
                print(f"{self.name} did not eat {food.name}.")
                self.alive = False


class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} ate {food.name}")
                self.fed = True
            else:
                print(f"{self.name} did not eat {food.name}.")
                self.alive = False


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name, edible=False)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)


a1 = Predator('The Wolf of Wall Street')
a2 = Mammal('Hachiko')
p1 = Flower('The Flower of Seven Flowers')
p2 = Fruit('A Clockwork Orange')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
