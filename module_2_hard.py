
n = input('Введите число от 3 до 20: ')
n = int(n)

def podbor(n):
    deliteli = []
    for i in range(2, n+1):
        if n / i == n // i:
            deliteli.append(i)
    password = []
    for j in range(len(deliteli)):
        a = 1
        b = deliteli[j] - 1

        while a < b:
            password.append(a)
            password.append(b)
            a += 1
            b -= 1

    return password


print(podbor(n))
spisok = "".join(map(str, podbor(n)))

print(spisok)

