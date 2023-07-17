file1 = open("x",'rb')
file2 = open("y",'wb')

for data in file1:
    file2.write(data)
    
    