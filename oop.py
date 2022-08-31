from unicodedata import name


class Apartments:
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location


class Units(Apartments):
    def __init__(self, name, location, floors) -> None:
        super().__init__(name, location)
        self.floors = floors

class Distance(Apartments):
    def giveDistance(self, distance):
        return "The distance from here is " + str(distance) + "KMs"

first = Units("Mlolongo", "Masaku", 12)

second = Distance("Dimples", "Karatina")
third = Distance("Victorias", "Town campus")

print(second.giveDistance(50))
print(first.floors)
