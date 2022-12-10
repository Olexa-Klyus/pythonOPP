import os, sys

# файли є текстові і двійкові
# імя файла є відносне (до директоріЇ) і абсолютне (повне)
# current working directory - поточна директорія
print(os.getcwd())

# для роботи файл потрібно відкрити
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# r читання, w перезапис або створення нового, a додавання в кінець
# rb - читання бінарного

f = open('test.txt', 'w', encoding='utf-8')
f.write('Alex\n')
f.write('Python')

x = ['1', '2', '3', '4']
f.write(f'{x}\n')  # - запише [1, 2, 3, 4]
f.writelines(x)  # - запише 1234

f.flush()  # - переносить на диск дані з памяті
f.close()
# якщо файл не закрити, ним ніхто не зможе користуватися
# EOF - флаг кінця файлу

# відкриття файлу з with - файл закриється автоматично
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Alex\n')
    f.write('Python')
    # числа у файл не запишеш
    x = [1, 2, 3, 4]
    # потрібно через цикл і f-стрічку
    for item in x:
        f.write(f'{item}\n')


# можна переправити потік виведення у файл
# і вивести прінтом у файл
# f = open('temp.txt', 'w')
# sys.stdout = f
# print('Hello')

