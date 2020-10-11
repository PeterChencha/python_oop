"""
NAMING CONVENTIONS
Public -> memberName
Protected -> _memberName
Private -> __memberName
"""


class Car:
    numberOfWheels = 4
    _color = "Black"
    __yearOfManufacture = 2017


class BMW(Car):

    def __init__(self):
        print("Protected attribute color: ", self._color)


car = Car()
print("Public attribute numberOfWheels: ", car.numberOfWheels)
bmw = BMW()
"""BELOW SHOULD RETURN ERROR. THOUGH THERE IS A WORKAROUND"""
print("Private attribute yearOfManufacture: ", car.__yearOfManufacture)
"""THE WORKAROUND"""
print("Private attribute yearOfManufacture: ", car._Car__yearOfManufacture)
