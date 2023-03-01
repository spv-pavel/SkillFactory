class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


class Square:
    def __init__(self, width):
        self.width = width

    @property
    def get_area_square(self):
        return self.width ** 2

    # @get_area_square.setter
    # def get_area_square(self, value):
    #     self.width = value


class Circle:
    def __init__(self, a):
        self.a = a

    def get_area_circle(self):
        return (self.a ** 2) * 3.14


# rect_1 = Rectangle(3, 4)
# rect_2 = Rectangle(3, 4)
square_1 = Square(5)
square_2 = Square(10)
# circle_1 = Circle(1)
# circle_2 = Circle(2)
'''
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())

print(rect_1 == rect_2)
'''
square_1.width = 6
print(square_1.get_area_square)
# square_1 = 6
# print(square_1.get_area_square)