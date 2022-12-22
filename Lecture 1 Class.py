# Кожен обєкт має (інкапсулює в собі) якийсь стан state (властивості) і якусь поведінку behavion (методи або функції)
# інкапсуляція - це поєднання даних (властивостей) і методів опрацювання цих даних
# базові принципи ОПП - інкапсуляція, наслідування, поліморфізм.
# Є ще абстракція, тобто робота не з повним переліком властивостей обєкта, а тільки з тими які нам потрібні.

# клас - це шаблон, на базі якого створюються екземпляри класу
# або користувацький тип даних
# клас це також обєкт, займає область в памяті, тому говорити обєкт класу не коректно, краще екземпляр класу
# тобто
# instans на базі template

class Student:
    pass


print(type(Student))  # виводить <class 'type'>

# Виводять різні id - посилання на різні області памяті
print(id(Student))

stud_1 = Student()
stud_2 = Student()
print(id(stud_1))
print(id(stud_2))


# є констуктор класу, метод init в Python

# self це показник на область памяті інстансу
# в кожному інстансі є зашитий id

class Student1:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

        print(id(self))
        print(self)


stud_3 = Student1('Ivanov', 'Ivan')
print(id(stud_3))

stud_4 = Student1('Petrov', 'Petro')
print(id(stud_4))

print(stud_3.surname, stud_3.name)
print(stud_4.surname, stud_4.name)


# є ще обовязковий метод __str__ , який використовується для повернення стрічкового представлення обєкта

class Student3:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


stud_5 = Student3('Lolita', 'Lola')
stud_3 = Student3('Ivanov', 'Ivan')
stud_4 = Student3('Petrov', 'Petro')



print(stud_5)

# атрибути класу зберігаються під капотом в словнику

print(dir(stud_5))
print(stud_5.__dict__)

# стан будь якого класу можна передати в словник і передати кудись
# відмінність стану(словника) від обєкту, що обєкт має поведінку

# можна в інстанс класу динамічно додавати атрибути
stud_5.age = 21
print(stud_5.__dict__)


# якщо потрібно додати студента в групу, потрібно створити клас Group
class Group:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    # повертаємо назву групи і список всіх студентів
    def __str__(self):
        return f'{self.title}\n{"-" * 10}\n' + '\n'.join(map(str, self.students))+'\n'


group_python = Group('Python IT')
group_python.add_student(stud_3)
group_python.add_student(stud_4)
group_python.add_student(stud_5)

group_english = Group('English IT')
group_english.add_student(stud_3)
group_english.add_student(stud_4)

print(group_python)
print(group_english)
print(group_python.__dict__)
print(group_english.__dict__)


