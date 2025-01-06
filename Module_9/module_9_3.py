
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_list = zip(first, second)

first_result = []
for i in list(first_list):
    if len(i[0]) != len(i[1]):
        div_ = len(i[0]) - len(i[1])
        first_result.append(div_)

second_result = []
for i in range(len(first)):
    res = len(first[i]) == len(second[i])
    second_result.append(res)


print(first_result)
print(second_result)