from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()  # Initialize the parent Thread class
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            remaining_enemies = max(0, self.enemies)
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")
