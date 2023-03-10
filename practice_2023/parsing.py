import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.zubron.ru/').content  # получим html главной странички официального сайта python

tree = lxml.html.document_fromstring(html)
title = tree.xpath(
    '/html/head/title/text()')
# забираем текст тега <title> из тега <head>, который лежит в свою очередь внутри тега <html>
# (в этом невидимом теге <head> у нас хранится основная информация о страничке, её название и инструкции по отображению
# в браузере)

print(title)  # выводим полученный заголовок страницы
print(tree)
