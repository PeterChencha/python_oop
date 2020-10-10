"""
Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a
given point of time. If there are more than 5 precious stones,
delete the first stone and store the new one.
"""


class Stone(object):
    """docstring for Stone."""

    def __init__(self):
        super(Stone, self).__init__()
        self.stones = []

    def addStone(self, name):
        if len(self.stones) >= 5:
            del self.stones[0]
            self.stones.append(name)
        else:
            self.stones.append(name)

    def stones_available(self):
        for stone in self.stones:
            print(stone)


stones = Stone()
stones.addStone("Diamond")
stones.addStone("Topaz")
stones.addStone("Ruby")
stones.addStone("Emerald")
stones.addStone("Saphire")
stones.stones_available()
stones.addStone("Carbuncle")
print("###########")
stones.stones_available()
