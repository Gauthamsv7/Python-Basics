class Computer:
    def __init__(self):
        self.name = "Gautham"
        self.age = 28
    def update(self):
        self.age = 35
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

com1 = Computer()
com2 = Computer()

com1.name = "Batman"
com2.age = 30

com1.update()
print(com1.name)
print(com1.age)
print(com2.name)
print(com2.age)

if com1.compare(com2):
    print("They are same")
else:
    print("They are different")