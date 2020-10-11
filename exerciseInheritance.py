"""
Write an object oriented program that performs the following tasks:
1. Create a class called Chair from the base class Furniture
2. Teakwood should be the type of furniture that is used by all furnitures by
default
3. The user can be given an option to change the type of wood used for chair if
he wishes to
4. The number of legs of a chair should be a property that should'nt be altered
outside the class
"""


class Furniture:
    typeOfMaterial = "Teakwood"


class Chair(Furniture):
    __numberOfLegs = 4

    def changeWood(self, material):
        self.typeOfMaterial = material


chair = Chair()
print(chair.typeOfMaterial)
chair.changeWood("Oak")
print(chair.typeOfMaterial)
