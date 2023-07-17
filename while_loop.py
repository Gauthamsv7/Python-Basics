#While loop

""" 


i = 3 
while (i < 6):
    print(i)
    i +=1
    
    
"""

num = int(input("Please enter the number : "))
count = 0
while count <= 10:
    product = num * count
    print(num,"x",count,"=",product)
    count = count+1