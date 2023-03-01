f = open('test.txt', 'w', encoding='utf8')

# Запишем в файл строку
f.write("This is a test string\n")
f.write("This is a new string\n")
f.close()

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
f.close()

f = open('test.txt', 'r', encoding='utf8')
print(f.readlines())  # считывает все строки в список и возвращает список
f.close()

f = open('test.txt', 'r', encoding='utf8')
print(f.readline())  # This is a test string
print(f.read(4))  # This
print(f.readline())  # is a new string
f.close()
