class Car:
    def model(self):
        print("BMW M5 car")

class CarF(Car):
    def model(self):
        print("Tesla S2 Car")

x =CarF()
x.model()