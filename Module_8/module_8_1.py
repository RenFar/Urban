while True:
    def add_everything_up(a, b):
        try:
            res = float(a) + float(b)

        except ValueError:
            res = a + b

        finally:
            print ('Итого:')

        return res


    a = input('Введите первое слогаемое: ')
    b = input('Введите второе слагаемое: ')

    print(add_everything_up(a, b))