from abc import ABC, abstractmethod
import math
# =========================
# PRODUCT INTERFACES
# =========================
class FlatShape(ABC):
 @abstractmethod
 def area(self):
  pass
 @abstractmethod
 def perimeter(self):
  pass
class SolidShape(ABC):
 @abstractmethod
 def volume(self):
  pass
 @abstractmethod
 def surface_area(self):
  pass
# =========================
# 2D PRODUCTS
# =========================
class Circle2D(FlatShape):
 def __init__(self, r):
  self.r = r
 def area(self):
  return math.pi * self.r ** 2
 def perimeter(self):
  return 2 * math.pi * self.r
class Square2D(FlatShape):
 def __init__(self, s):
  self.s = s
 def area(self):
  return self.s ** 2
 def perimeter(self):
  return 4 * self.s
# =========================
# 3D PRODUCTS
# =========================
class Sphere3D(SolidShape):
 def __init__(self, r):
  self.r = r
 def volume(self):
  return (4/3) * math.pi * self.r ** 3
 def surface_area(self):
  return 4 * math.pi * self.r ** 2
class Cube3D(SolidShape):
 def __init__(self, s):
  self.s = s
 def volume(self):
  return self.s ** 3
 def surface_area(self):
  return 6 * self.s ** 2
# =========================
# ABSTRACT FACTORY
# =========================
class ShapeFactory(ABC):
 @abstractmethod
 def create_flatshape(self):
  pass
 @abstractmethod
 def create_solidshape(self):
  pass
# =========================
# CONCRETE FACTORIES
# =========================
class CircleSphereFactory(ShapeFactory):
 def create_flatshape(self):
  r = float(input("Enter radius: "))
  return Circle2D(r)
 def create_solidshape(self):
  r = float(input("Enter radius: "))
  return Sphere3D(r)
class SquareCubeFactory(ShapeFactory):
 def create_flatshape(self):
  s = float(input("Enter side: "))
  return Square2D(s)
 def create_solidshape(self):
  s = float(input("Enter side: "))
  return Cube3D(s)
# =========================
# FACTORY PRODUCER
# =========================
class Factory:
 def createFactory(choice):
  if choice == "circle":
   return CircleSphereFactory()
  elif choice == "square":
   return SquareCubeFactory()
  return None
# =========================
# CLIENT
# =========================
def client():
 choice = input("Enter shape (circle / square): ").lower()
 factory = Factory.createFactory(choice)
 dimension = input("Enter dimension (flat / solid): ").lower()
 if dimension == "flat":
   shape = factory.create_flatshape()
   print("\nArea: ", round(shape.area(), 4))
   print("Perimeter:", round(shape.perimeter(), 4))
 elif dimension == "solid":
   solid = factory.create_solidshape()
   print("\nVolume: ", round(solid.volume(), 4))
   print("Surface area:", round(solid.surface_area(), 4))
 else:
  print("Invalid dimension")
# RUN
client()