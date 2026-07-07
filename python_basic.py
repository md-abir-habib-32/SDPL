class Person:
    name = "abir"
    occupa = "student"
    age = 20
    def info(self):
        print(f"{self.name} is a {self.occupa}")

a = Person()
b= Person()

a.name ="Habib"
a.occupa = "ST"
b.name ="Asif"
b.occupa ="manager"

#print(a.name, a.occupa)
a.info()
b.info()