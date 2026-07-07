from abc import ABC, abstractmethod
# Abstract class with an abstract method
class Vehicle(ABC):
 def __init__(self, name):
  self.name = name
 @abstractmethod
 def start(self):
  pass
 @abstractmethod
 def stop(self):
  pass
# Concrete class extending the abstract class
class Car(Vehicle):
 def start(self):
  return f"{self.name} started"
 def stop(self):
  return f"{self.name} stopped"
# Creating instances of the concrete class
car = Car("Audi")
print(car.start())
print(car.stop())