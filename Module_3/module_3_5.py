
def get_multiplied_didgits(number):
    str_number = str(number)
    first = str_number[0]
    return first * get_multiplied_didgits(int(str_number[1:]))
    second = int(str_number[1])
    print(str_number)
    print(first)
    print(second)
    str_number = int(str_number)
    print(str_number)




print(get_multiplied_didgits(90502))


