#Namespace is an area where you create and store object/Variable
#Class namespace
#Object/Instance namespace

class Car:

    wheels = 4 #Class namespace

    def __init__(self):  #Object/Instance namespace
        self.mil = 10
        self.com = "BMW"



c1 = Car()
c2 = Car()


c1.mil = 8
c2.wheels = 60
Car.wheels = 5

print(c1.com,c1.mil,c1.wheels)
print(c1.com,c2.mil,c2.wheels)