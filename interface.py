from abc import ABC, abstractmethod
# Creating an interface-like structure using abstract base class
class Shape(ABC):
 @abstractmethod
 def calculate_area(self):
  pass
 @abstractmethod
 def calculate_perimeter(self):
  pass
# Implementing the interface in a class
class Square(Shape):
 def __init__(self, size):
  self.size = size
 def calculate_area(self):
  return self.size * self.size
 def calculate_perimeter(self):
  return 4 * self.size
# Using the Square class which implements the 'Shape' interface
square = Square(5)
print("Area:", square.calculate_area())
print("Perimeter:", square.calculate_perimeter())