class A: #superclass
    def __init__(self):
        print("In A Init")

    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")

class B(A): #subclass A->B
    def __init__(self):
        super().__init__() #representing the superclass and calling them
        print("In B Init")
    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")

class C():
    def __init__(self):
        print("In C Init")
    def feature1(self):
        print("Feature1-B working")
    def feature2(self):
        print("Feature2-B working")

'''MRO:Method Resolution Order : It works during multiple inheritance
it starts taking from left to right'''
class D(A,C): #subclass A->D,C->D
    def __init__(self):
        super().__init__()
        print("in D init")
    def feature7(self):
        super().feature2() #Super method can be used to call super class methods
a1 = D()
a1.feature7()