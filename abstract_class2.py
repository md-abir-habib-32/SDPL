from abc import ABC,abstractmethod
class vechical(ABC):

    def __init__(self,name):
        self.name=name
    @abstractmethod
    def  start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(vechical):
    def start(self):
        return(F"Started {self.name}")
    def stop(self):
        return(F"stopped {self.name}")

g=Car("BMW")
print(g.start())
print(g.stop())

