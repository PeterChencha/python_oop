from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def area(self):
        pass


class Square(object):
    """docstring for Square."""

    def __init__(self):
        super(Square, self).__init__()
        self.arg = 5

    def area(self):
        print("Area of a square is ", self.arg * self.arg)


class Rectangle(object):
    """docstring for Rectangle."""

    def __init__(self):
        super(Rectangle, self).__init__()
        self.length = 5
        self.width = 10

    def area(self):
        print("Area of rectangle is ", self.width * self.length)


square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
