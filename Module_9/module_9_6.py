def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        prime = False
        for i in range(2, number):
            a = number / i == number // i
            prime = a or prime
        if prime == False:
            print("Простое")
        else:
            print("Составное")
        return number
    return wrapper



@is_prime
def sum_three(*args):
    summ = 0
    for i in args:
        summ += i
    return summ



result = sum_three(2, 3, 6)

print(result)