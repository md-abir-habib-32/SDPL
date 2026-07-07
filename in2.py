from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def cal_area(self):
        pass
    @abstractmethod
    def cal_peramiter(self):
        pass

class Rectan(Shape):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def cal_area(self):
        return self.x * self.y
    def cal_peramiter(self):
        return 2*(self.x + self.y)

A=Rectan(10,10)
print("Area= ",A.cal_area())
print("Peramitar= ",A.cal_peramiter())


