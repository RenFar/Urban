class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        print(args)
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'




h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
