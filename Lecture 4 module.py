# модуль - це теж обєкт, який має свій простір імен.
# імпортінг модулів - це процес, який робить доступним код пайтону з іншого модуля.

import sys
import math

print(sys.stdlib_module_names)
# константа, яка виводить
# перелік всіх стандартних модулів, які є у пайтоні
# у вигляді немутованої множини - нічого не можемо додати чи забрати

print(sys.builtin_module_names)
# константа, яка виводить
# перелік всіх вбудованих модулв як кортеж

# модулі теж мають різні атрибути
print(math.__name__)
print(math.__doc__)

# всі атрибути модуля є у відповідному словнику
print(math.__dict__)
# який можна змінити


# модуль завантажується в память один раз, при першому імпорті, навіть якщо імпортів декілька,
# додається ключ в словнику sys.modules, створюється змінна, яка посилається на цей модуль
# щоб його перезантажити (наприклад зі змінами), є спец функція reload

# процес імпортінгу можна записати під капотом - наприклад спробуємо імпортнути Lecture 2 HW.py
from types import ModuleType

import_module = 'Lecture 2 HW'
if import_module not in sys.modules:
    sys.modules[import_module] = ModuleType(import_module)  # створюємо інстанс класу  ModuleType
    code = open(import_module + '.py', 'rb').read()         # зчитуємо модуль з файлу як бінарний файл
    exec(code, sys.modules[import_module].__dict__)         # виконуємо, реєструємо в словнику sys.modules

lec2_HW = sys.modules[import_module]

stud1 = lec2_HW.Student('Ivan5', 'Ivanov5', 445)

group1 = lec2_HW.Group('Python', 5)
group1.add_student(stud1)

res = group1.search_student('Ivanov1')
print(group1)


print(sys.modules[import_module].__dict__)

# всі модулі, які завантажені в оперативну память,(включаючи імпортовані),  і їхнє розташування на диску є у відповідному словнику
for item in sys.modules:
    print(item, ' - ', sys.modules[item])

# при імпортінгу весь модуль виконується !!!, навіть якщо імпортуємо одну функцію
