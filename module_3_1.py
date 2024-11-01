calls = 0
def count_calls():                              # функция для подсчета количества вызовов
    global calls
    calls += 1                                  # подсчет количества вызовов

def string_info(word):                          # функция для подсчета длины слова и перевода его в верхний и нижний регистры
    string_1=[]
    string_1.append(len(word))                  # добавление в спосок длины слова
    upp = word.upper()                          # перевод в верхний регистр
    low = word.lower()                          # перевод в нижний регистр
    string_1.append(upp)                        # добавление к списку слова в верхнем регистре
    string_1.append(low)                        # добавление к списку слова в нижнем регистре
    print(string_1)                             # выводим результат
    count_calls()                               # вызов функции count_calls для добавления к счетчику

def is_contains(string_, spisok):               # функция проферки на совпадение
    low = string_.lower()                       # перевод в нижний регистр первой стороки для сравнения
    spisok_new = []
    for i in range(len(spisok)):                # цикл для перевода всех слов списка в нижний регистр для сравнения
        low_1 = spisok[i].lower()
        spisok_new.append(low_1)
    probe = False
    for j in range(len(spisok_new)):            # цикл для сравнения первой строки со словами из списка
        proverka = (low == spisok_new[j])
        result = probe or proverka
    count_calls()                               # вызов функции count_calls для добавления к счетчику
    print(result)


string_info('Abrakadabra')
string_info('Chupacabra')
string_info('ChuBaka')
is_contains('Banan', ['Nan', 'Apple', 'banan'])
is_contains('Goblin', ['Blin', 'Orange', 'Loop'])
is_contains('Urban', ['Cosmos', 'Sun', 'UrBaN'])
print(calls)


