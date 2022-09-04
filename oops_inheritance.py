''' Subclass can access all the features of Super class,
but
Super class cannot access any features of subclass'''


class A: #superclass
    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")

class B(A): #subclass A->B
    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")

class C(B): #Multilevelclass A->B->C
    def feature5(self):
        print("Feature5 working")
    def feature6(self):
        print("Feature6 working")

class D(): #Standalone
    def feature7(self):
        print("Feature7 working")
    def feature8(self):
        print("Feature8 working")

class E(A,D): #Multiple_class A->E, D->E
    def feature9(self):
        print("Feature9 working")
    def feature10(self):
        print("Feature10 working")


a1 = A()

a1.feature1()
a1.feature2()

b1 =B()
b1.feature3()
b1.feature4()

c1 =C()
c1.feature1()
c1.feature3()