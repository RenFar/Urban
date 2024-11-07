def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2, 'столбец',  False)
print_params(b= 25)
print_params(c=[1, 2, 3])

values_list= (3, 'строчка', False)
values_dict= {"a": 4, 'b': 'столбик', "c": True}
print_params(*values_list)
print_params(**values_dict)

values_list_2= (5, "строка или стобец")
print_params(*values_list_2, 42)
