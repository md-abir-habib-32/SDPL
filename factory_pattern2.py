from abc import ABC,abstractmethod

from factory_pattern import Square


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return("Inside Circle:Draw Method")
class Rec(Shape):
    def draw(self):
        return("Inside rectangle:Draw method ")
class Square(Shape):
    def draw(self):
        return("Inside square:Draw method ")


class ShapeFactory(Shape):
    def getShape(self,name):

     if name == "Circle":
        return Circle()
     elif name =="Rec":
         return Rec()
     elif name =="Square":
         return Square()


def ShapeClient():
    x= ShapeFactory()
    shapeName = input("Enter the name of the shape: ")
    shape=x.getShape(shapeName)
    shape.draw()
    ShapeClient()



