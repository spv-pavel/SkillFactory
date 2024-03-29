G = {"Лиговский проспект":
         ["Площадь Александра Невского 2"],
     "Площадь Александра Невского 2":
         ["Площадь Александра Невского 1",
          "Лиговский проспект",
          "Новочеркасская"],
     "Площадь Александра Невского 1":
         ["Площадь Александра Невского 2",
          "Елизаровская"],
     "Новочеркасская":
         ["Площадь Александра Невского 2",
          "Ладожская"],
     "Ладожская":
         ["Новочеркасская",
          "Проспект Большевиков"],
     "Проспект Большевиков":
         ["Ладожская",
          "Дыбенко"],
     "Дыбенко":
         ["Проспект Большевиков"],
     "Елизаровская":
     ["Площадь Александра Невского 1"]}

D = {k: 100 for k in G.keys()}  # расстояния
start_k = 'Адмиралтейская'  # стартовая вершина
D[start_k] = 0  # расстояние от неё до самой себя равно нулю
U = {k: False for k in G.keys()}  # флаги просмотра вершин
P = {k: None for k in G.keys()}  # предки

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key=lambda x: D[x])

    for v in G[min_k].keys():  # проходимся по всем смежным вершинам
        if D[v] > D[min_k] + G[min_k][v]:  # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v]  # то фиксируем его
            P[v] = min_k  # и записываем как предок
    U[min_k] = True  # просмотренную вершину помечаем

some_station = "Новочеркасская"
pointer = some_station  # куда должны прийти
path = []  # список с вершинами пути
while pointer is not None:  # перемещаемся, пока не придём в стартовую точку
    path.append(pointer)
    pointer = P[pointer]

path.reverse()  # разворачиваем путь
for v in path:
    print(v)
