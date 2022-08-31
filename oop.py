# single inheritance


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


# multiple inheritance

class BioData:
    def __init__(self, firstName, lastName) -> None:
        self.firstName = firstName
        self.lastName = lastName

class Course:
    course = "Computer Science"

class FullData(BioData, Course):
    pass

someData = FullData("Paul", "Mutemi")
print("Hello, my name is " + someData.firstName, someData.lastName + ".I take", someData.course)


# Multi-level inheritance example
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)

"""
The o​utput is 2 because C derives from the immediate super class of C, and that's B.

The case above is an example of multi-level inheritance where the derived class C inherits from base class B. 
The class B is in turn a derived class of base class C. Class B here is an intermediary derived class. 
There are three levels of inheritance in this case, but it could be extended as long as I want, though it may become impractical after a while.
"""