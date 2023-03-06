import requests
import json

# data = {'key': 'value'}

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)
print(type(texts))
print(texts[0])

# -----------------------------------------------------------
# r = requests.get('https://api.github.com')
# d = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы
# print(type(d))
# print(d['following_url'])
# # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

# -----------------------------------------------------------
# r = requests.post('https://httpbin.org/post', data = {'key':'value'})  # отправляем POST-запрос
# print(r.content)  # содержимое ответа и его обработка происходит так же, как и с GET-запросами, разницы никакой нет

# -----------------------------------------------------------
# data = {'key': 'value'}
# r = requests.post('https://httpbin.org/post', json=json.dumps(
#     data))  # отправляем POST-запрос, но только в этот раз тип передаваемых данных будет JSON
# print(r.content)
