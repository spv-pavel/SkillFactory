f = open('test.txt', 'w', encoding='utf8')
print(f.tell())  # указатель на позицию в файле
# Запишем в файл строку
f.write("This is a test string\n")
f.write("This is a new string\n")
print(f.tell())
f.close()  # до этого записанные данные хранились RAM, после выполнения этой команды записались на диск.

# f = open('test.txt', 'r', encoding='utf8')
# print(f.read())

# f = open('test.txt', 'r', encoding='utf8')
# print(f.read(10))
# print()
# print(f.read())
# f.close()

f = open('test.txt', 'a', encoding='utf8')  # открываем файл на дозапись
sequence = ["other string\n", "123\n", "test test\n"]
f.writelines(sequence)  # берёт строки из sequence и записывает в файл (без переносов)
print(f.tell())
f.close()

# f = open('test.txt', 'r', encoding='utf8')
# print(f.readlines())  # считывает все строки в список и возвращает список
# print(f.tell())
# f.close()

# f = open('test.txt', 'r', encoding='utf8')
# print(f.readline())  # This is a test string
# print(f.tell())
# print(f.read(4))  # This
# print(f.tell())
# print(f.readline())  # is a new string
# print(f.tell())
# f.close()

print('================')
# f = open('test.txt', 'r')
# f.seek(1)
# print(f.tell())
# f.close()

f = open('test.txt')
for line in f:
    print(line.strip())

with open('test.txt', 'rb') as f:
    a = f.read(10)
    b = f.read(23)
# автоматически файл закрывается без f.close()

# Создайте любой файл на операционной системе под название input.txt и построчно перепишите его в файл output.txt.
with open('input.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        for line in input_file:
            output_file.write(line)

 """Дан файл numbers.txt, компоненты которого являются действительными числами
 (файл создайте самостоятельно и заполните любыми числами, в одной строке одно число).
Найдите сумму наибольшего и наименьшего из значений и запишите результат в файл output.txt."""
filename = 'numbers.txt'
output = 'output.txt'

# with open(filename) as f:
#    min_ = max_ = float(f.readline())  # считали первое число
#    for line in f:
#        num =  float(line)
#        if num > max_:
#            max_ = num
#        elif num < min_:
#            min_ = num
#
#    sum_ = min_ + max_
#
# with open(output, 'w') as f:
#    f.write(str(sum_))
#    f.write('\n')

"""В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за контрольную.
Выведите на экран всех учащихся, чья оценка меньше 3 баллов. Cодержание файла:"""
# Иванов О. 4
# Петров И. 3
# Дмитриев Н. 2
# Смирнова О. 4
# Керченских В. 5
# Котов Д. 2
# Бирюкова Н. 1
# Данилов П. 3
# Аранских В. 5
# Лемонов Ю. 2
# Олегова К. 4

# with open('input.txt', encoding="utf8") as file:
#     for line in file:
#         points = int(line.split()[-1])
#         if points < 3:
#             name = " ".join(line.split()[:-1])
#             print(name)

#  Выполните реверсирование строк файла (перестановка строк файла в обратном порядке).
# with open('input.txt', 'r') as input_file:
#    with open('output.txt', 'w') as output_file:
#        for line in reversed(input_file.readlines()):
#            output_file.write(line)
