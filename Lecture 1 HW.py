class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title} : {self.price}'


class Customer:
    def __init__(self, surname: str, name: str, phone: str):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name} ; {self.phone}'


class Cart:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: float = 1):

        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)


def total(self):
    # summa = 0
    # for index, item in enumerate(self.products):
    #     summa += item.price * self.quantities[index]
    # return summa

    # або
    return sum(item.price * self.quantities[index] for index, item in enumerate(self.products))


def __str__(self):
    # res = ''
    # for index, item in enumerate(self.products):
    #     res += f'{item} x {self.quantities[index]} = {item.price * self.quantities[index]} UAH\n'
    # return res

    # або
    # res = ''
    # for item, quantity in zip(self.products, self.quantities):
    #     res += f'{item} x {quantity} = {item.price * quantity} UAH\n'
    # return res

    # або так - zip повертає кортеж з n-го елемента продуктів і n-го елемента кількості
    res = '\n'.join(map(
        lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
        zip(self.products, self.quantities))
    )

    return f'{customer}\n{res}\nTotal : {self.total()} UAH'


apple = Product('apple', 15)
banana = Product('banana', 45)
orange = Product('orange', 60)

customer = Customer('Petrov', 'Petro', '06769439876')

order = Cart(customer)
order.add_product(apple, 3)
order.add_product(banana)
order.add_product(orange, 0.5)

print(order)

# атрибути бувають

# public наприклад order.products
# print(order.products)
# print(order.quantities)

# private, наприклад __order.products, до яких нема доступу зовні і які не виведуться на друк
# print(order.__products)
# print(order.__quantities)

# але можна отримати доступ через таку конструкцію
# order._Cart__products
# але так робити не треба