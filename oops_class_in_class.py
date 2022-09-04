class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() #Intiate here itself

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 16
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = Student("Gautham", 2)
s2 = Student("Batman", 3)

s1.show()
lap1 = Student.Laptop()
lap2 = s2.lap

print(id(lap1))
print(id(lap2))