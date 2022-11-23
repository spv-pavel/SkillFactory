from myclass import Client

c1 = Client('Иван', 'Петров', 'Москва', 50)
c2 = Client('Павел', 'Смирнов', 'Владимир', 150)
c3 = Client('Алексендр', 'Иванов', 'Рязань', 56)
clients = [c1, c2, c3]
# print(clients[1])

for client in clients:
    print(client.get_client())
# print(c1)