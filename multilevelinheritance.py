class MusicalInstrument:
    numberOfMajorKeys = 12


class StringInstrument(MusicalInstrument):
    typeOfWood = "Tonewood"


class Guitar(StringInstrument):

    def __init__(self):
        self.numberOfStrings = 6
        print("This guitar has {} strings, made of {} and can play {} keys".
              format(self.numberOfStrings, self.typeOfWood,
                     self.numberOfMajorKeys))


guitar = Guitar()
