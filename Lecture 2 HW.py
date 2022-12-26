class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Student(Human):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, {self.age}'


class Group:
    def __init__(self, title, max_students=10):
        self.title = title
        self.__students = []
        self.max_student = max_students

    def __str__(self):
        return f'{self.title}\n{"*" * 10}\n' + '\n'.join(map(str, self.__students))

    def add_student(self, student):
        if student not in self.__students and len(self.__students) < self.max_student:
            self.__students.append(student)

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)

    def search_student(self, surname):
        res = []
        for student in self.__students:
            if student.surname == surname:
                res.append(student)
        return res


stud1 = Student('Ivan1', 'Ivanov1', 15)
stud2 = Student('Ivan2', 'Ivanov2', 25)
stud3 = Student('Ivan3', 'Ivanov3', 35)
stud4 = Student('Ivan4', 'Ivanov4', 45)

group1 = Group('Python', 5)
group1.add_student(stud1)
group1.add_student(stud2)
group1.add_student(stud3)
group1.add_student(stud4)

res = group1.search_student('Ivanov1')
print(group1)

for item in res:
    print(item)
