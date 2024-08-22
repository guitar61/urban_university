import random


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything()


first_ball = MysticBall('Yes', 'No', 'Probably')
print(first_ball())
print(first_ball())
print(first_ball())
