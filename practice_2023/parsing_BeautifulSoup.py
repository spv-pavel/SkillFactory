from bs4 import BeautifulSoup
import requests


def main():
    base = 'https://ru.stackoverflow.com/'
    html = requests.get(base).content
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', id='question-mini-list')
    a = div.find_all('a', class_='s-link')
    for _ in a:
        # print(base + _.get('href'))
        print(_.getText(), base + _.get('href'))


if __name__ == '__main__':
    main()
