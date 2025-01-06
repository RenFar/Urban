import codecs
from random import choice


first = 'Мама мыла раму'
second = 'Рамена мало было'

chars_1_2 = lambda first, second: list(map(lambda char_1, char_2: char_1 == char_2, first, second))

result = chars_1_2(first, second)
print(result)




def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with codecs.open(file_name, 'a', encoding='utf-8') as app_to_file:
            for data in data_set:
                app_to_file.write(str(data) + '\n')

    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')

write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
write('Это ещё строчка', ['И', 'это', 'уже', 'слово', "пять", 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())