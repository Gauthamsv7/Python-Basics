#Abstract class cannot have object
#Abstract class is used when we write the code in OOOPs way.
#ABC means abstract base classes
from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        print("Running")

class Laptop(Computer):
    def process(self):
        print("Lets run")
class Programmer:
    def work(self,comp):
        print("Solving Bugs")
        com1.process()
class Whiteboard(Computer):
    def write(self):
        print("its writing")


#com = Computer()
com1 = Laptop()
com2 = Whiteboard()
#com1.process()
prog1 = Programmer()
#prog1.work(com1)
prog1.work(com2)
#com.process()

