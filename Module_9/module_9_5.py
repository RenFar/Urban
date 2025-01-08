
class Iterator:

    def __init__(self, start, stop, step = 1):
        if step == 0:
            print('шаг не может быть равен 0')
            raise StepValueError()
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start



    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.stop > self.start:
            if self.pointer > self.stop:
                raise StopIteration
            elif self.pointer <= self.stop:
                result = self.pointer
                self.pointer += self.step
                if self.pointer < self.start:
                    print(f'Шаг указан неверно, начало: {self.start}, конец: {self.stop}, шаг: {self.step}')
                    raise StopIteration
                else:
                    return result
        elif self.stop < self.start:
            if self.pointer < self.stop:
                raise StopIteration
            elif self.pointer >= self.stop:
                result = self.pointer
                self.pointer += self.step
                if self.pointer > self.start:
                    print(f'Шаг указан неверно, начало: {self.start}, конец: {self.stop}, шаг: {self.step}')
                    raise StopIteration
                else:
                    return result
class StepValueError(ValueError):
    pass
    #print('Шаг указан неверно')


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
    print()
print("----------")
for i in iter3:
    print(i, end=' ')
    print()
print("----------")
for i in iter4:
    print(i, end=' ')
    print()
print("----------")
for i in iter5:
    print(i, end=' ')
    print()