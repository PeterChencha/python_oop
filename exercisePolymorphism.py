"""
Create a class called Square and perform the following tasks -
(i) Create two objects for this class squareOne and
squareTwo
(ii) Find the result of side of squareOne to the power of side
of squareTwo
Example: If squareOne has length of 2cm each side and
squareTwo has a length of 4cm each side, squareOne **
squareTwo should return 16, which is 2 to the power of 4.
"""


class Square(object):
    """docstring for Square."""

    def __init__(self, side):
        super(Square, self).__init__()
        self.side = side

    def __pow__(squareOne, squareTwo):
        return((pow(squareOne.side, squareTwo.side)))


squareOne = Square(2)
squareTwo = Square(4)

print("Square of the squares is ", pow(squareOne, squareTwo))
