'''Polymorphism:One thing having many forms
Types to perform:
1.Duck typing
2.Operator Overloading
3.Method Overloading
4.Method Over-riding'''

#Duck Typing

class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
class Editor:
    def execute(self):
        print("Compiling")
        print("Spell check")
        print("Executing")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()
ide = Editor()

lap1 = Laptop()
lap1.code(ide)


#Operator Overloading

