'''

Welcome to Python Roadmap Step-1 . Here we are about to learn few basics such as

1.Basic Syntax and Variables
2.Data Types
3.Conditions

Let's get started !!!

'''

#
# Variable
#

X = 300 #Assigning some info to a specific thing is called a Variable.

#Variables can be converted accordingly

x1 = str(X)
x2 = int(X)
x3 = float(X)

print("x1 is : ",type(x1)," and x2 is :",type(x2)," and x3 is : ",type(x3))


#Assigning Variables

x,y,z = "Apple","Ball","Cat"

print(x)
print(y)
print(z)

#Assigning one value to Multi variables
A = ["Soccer"]
a=b=c = A

print(a)
print(b)
print(c)


#Using + to merge two variables
#Works with Strings + Strings or Int + Int

a1 = "Batman"
a2 = "is"
a3 = "The"
a4 = "Best"

a5 = a1+a2+a3+a4
print(a5)


#Trivia : Some of you have wondered about Global variable vs self(instance variable) .Best practice is to use self always for better coding.

#
# Data Types
#