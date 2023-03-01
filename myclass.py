class Cat:
    def __init__(self, name='', age=0, gender=''):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender


class Dog(Cat):
    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'


class Rectangle:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'{self.x, self.y, self.width, self.height}'

    def get_square(self):
        return self.width * self.height


class Client:
    def __init__(self, name='-', surname='-', city='-', balance=0):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'

    def get_client(self):
        return f'{self.name} {self.surname}, {self.city}'

