#Step 1 (create an Interface)
import abc
class Shape(metaclass=abc.ABCMeta):
 @abc.abstractmethod
 def draw(self):
  pass
#Step 2 (Create concrete classes implementing the same interface)
class Rectangle(Shape):
 def draw(self):
  print("Inside Rectangle::Draw Method")
class Square(Shape):
 def draw(self):
  print("Inside Square::Draw Method")
class Circle(Shape):
 def draw(self):
  print("Inside Circle::Draw Method")
#Step 3 (Create a Factory to generate object of concrete classbased on given information.)
class ShapeFactory:
 def get_shape(self, name):
  if name == 'circle':
    return Circle()
  elif name == 'rectangle':
   return Rectangle()
  elif name == 'square':
   return Square()
#Step 4 (Use the Factory to get object of concrete class bypassing an information such as type.)
def shapes_client():
 shape_factory = ShapeFactory()
 shape_name = input("Enter the name of the shape: ")
 shape = shape_factory.get_shape(shape_name)
 shape.draw()
shapes_client()