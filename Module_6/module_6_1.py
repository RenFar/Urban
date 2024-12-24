from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight= weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'
        self.__products = []


    def get_products(self):
        product = open(self.__file_name, 'r')
        products_str = product.read()
        product.close()

        return products_str

    def add(self, *products):

        for product_ in products:
            if product_.name in self.__products:
                print(f"Продукт {product_.name} уже есть в магазине")
            else:

                with open(self.__file_name, 'a') as file:
                    file.write(str(product_) + "\n")

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')


print(p1, "\n")
print(p2, "\n") # __str__
print(p3, "\n")

print(s1.get_products(), "...\n")

s1.add(p1)
print(s1.get_products(), "...\n")
s1.add(p2)
print(s1.get_products(), "...\n")
s1.add(p3)

print(s1.get_products())