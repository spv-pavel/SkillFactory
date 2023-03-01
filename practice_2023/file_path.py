import os


def walk_desc(path=None):
    start_path = path if path is not None else os.getcwd()

    for root, dirs, files in os.walk(start_path):
        print("Текущая директория", root)
        print("---")

        if dirs:
            print("Список папок", dirs)
        else:
            print("Папок нет")
        print("---")

        if files:
            print("Список файлов", files)
        else:
            print("Файлов нет")
        print("---")

        if files and dirs:
            print("Все пути:")
        for f in files:
            print("Файл ", os.path.join(root, f))
        for d in dirs:
            print("Папка ", os.path.join(root, d))
        print("===")


os.chdir("..")
path1 = os.path.join(os.getcwd(), 'imports', 'practice_2022')
# path = os.path.join(path, 'mylibrary')
print(path1)
print(os.listdir())
print(os.path.exists('imports'))
print(os.path.exists('test.py'))
if 'test.py' in os.listdir():
    print(True)
# walk_desc()
