"""
write a program to
provide layers of abstraction for a car rental system.
Your program should perform the following:
1. Hatchback, Sedan, SUV should be type of cars that are
being provided for rent
2. Cost per day:
Hatchback - $30
Sedan - $50
SUV - $100
3. Give a prompt to the customer asking him the type of car
and the number of days he would like to borrow and provide the
fare details to the user.
"""


class Car(object):
    """docstring for Car."""

    def __init__(self, model, rate):
        super(Car, self).__init__()
        self.model = model
        self.rate = rate


class Shop(object):
    """docstring for Shop."""

    def __init__(self):
        super(Shop, self).__init__()
        self.name = "Chencha's Shop"
        self.availableCars = []

    def addCar(self, model, rate):
        car = Car(model, rate)
        self.availableCars.append(car)

    def viewAvailableCars(self):
        for car in self.availableCars:
            print(car.model, car.rate)

    def getRate(self, model):
        for car in self.availableCars:
            if car.model == model:
                return car.rate

    def calculateFareDetails(self, requestedModel, noOfDays):
        rate = self.getRate(requestedModel)
        fare = rate * noOfDays
        return fare


class Customer(object):
    """docstring for Customer."""

    def rentCar(self, request, days):
        shop = Shop()
        for car in shop.availableCars:
            if request == car.model:
                fair = shop.calculateFareDetails(request, days)
                return fair


shop = Shop()
shop.addCar("Hatchback", 30)
shop.addCar("Sedan", 50)
shop.addCar("Suv", 100)
customer = Customer()

while True:
    print("Enter 1 to display fare details")
    print("Enter 2 to rent a car")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice == 1:
        shop.viewAvailableCars()
    elif userChoice == 2:
        print("What model would you like to rent?")
        model = input()
        print("For how many days")
        days = int(input())
        fareDetails = shop.calculateFareDetails(model, days)
        print("Fare will be {}".format(fareDetails))
    elif userChoice == 3:
        quit()
