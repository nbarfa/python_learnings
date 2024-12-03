from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = int(input("Entre Length : "))
        self.breath = int(input("Entre Breath : "))

    def printarea(self):
        return f"The Area is {self.length * self.breath}"

rec1 = Rectangle()
print(rec1.printarea())

