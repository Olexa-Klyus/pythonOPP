# наслідування - це форма повторного використання коду на базі вже готового класу
# при цьому новий поглинає публічний і захищений інтерфейс базового класу та може розширювати його

# тобто методи базового класу ми можемо змінити, замінити, видалити, додати додаткові методи.

# тому що готовий клас не змінюємо, бо він протестований
# клас повинен бути open - close, тобто відкритий для розширення - закритий для змін

# батьківський клас може називатися -
# super, base, parrent
# дочірній -
# child, sub, derived

# звязок між батьківським і дочірнім - single inheritance
# звязок між дідвським, батьківським і дочірнім - multi level inheritance
# звязок між 2 батьками і дочірнім - multiple inheritance

class BaseA:
    def __init__(self):
        self.a = 10

    def method(self):
        return self.a


class SubB(BaseA):
    def __init__(self):
        # для того щоб успадкувалася змінна а з базового класу, потрібно в дочірньому класі викликати базовий, тоді вона ініціалізується
        super().__init__()
        self.b = 20

    def sub_method(self):
        return self.b

    # можна переписати метод з батьківського класу,а також звернутися до нього через функцію super()
    def method(self):
        return super().method() + self.b


x = SubB()
print(x.__dict__, x.a, x.b)
print(SubB.__dict__.keys())
print(SubB.__mro__)  # зберігає дерево класів у вигляді кортежу, в якому будуть шукатися методи
print(x.method())

# базові методи класу object
print('\n'.join(object.__dict__))


class A:
    def method(self):
        return 'Hello from A'


class B:
    def method(self):
        return 'Hello from B'


# якщо є успадкування від двох класів однакових методів, відпрацює той, який в дужках вказаний першим

class C(B, A):
    ...


y = C()
print(C.__mro__)
print(y.method())


# проблема ромбу якщо йде наслідування від одного і того ж класу двох класів, а потім третій клас від тих двох одночасно

class Exp1:
    def __init__(self, a):
        self.a = a


class Exp2(Exp1):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b


class Exp3(Exp1):
    def __init__(self, a, c):
        super().__init__(a)
        self.c = c


class Exp4(Exp2, Exp3):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        super().__init__(a, c)
        self.d = d


print(Exp4.__mro__)
x = Exp4(1, 2, 3, 4)
# print(x)
