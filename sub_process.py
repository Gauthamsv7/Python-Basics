import subprocess
import os
import glob

'''

Subprocess :
    > run : Will start process and wait until the new process exits before moving on.
    > Popen : 
    > call

'''



'''
run :

subprocess.run('ls -la',shell=True)   --->>> In the use of shell command
subprocess.run(['ls','-la'])          --->>> In the absence of shell command
p1=subprocess.run('ls -la',capture_output=True) --->>> Used to capture the Output of the program
print(p1.stdout.decode()) --->>> It will make sure that the Output is in arranged manner.

                        and 
                        
p1=subprocess.run('ls -la',capture_output=True,text=True)
print(p1.stdout)

                        and
                        
p1=subprocess.run('ls -la',stdout=subprocess.PIPE,text=True)
print(p1.stdout)

CAPTURE THE OUTPUT INTO A FILE

with open('output.txt','w') as f:
    p1=subprocess.run('ls -la',stdout=f,text=True)


                        and
                        
Error Case :

p1=subprocess.run('ls -la','dne',capture_output=True,text=True)
print(p1.stderr) --->>> To see the error.
                        and
p1=subprocess.run('ls -la','dne',capture_output=True,text=True,check=True) --->>> Saying python to throw an error .
print(p1.stderr)

                        and
                        
p1=subprocess.run('ls -la','dne',stderr=subprocess.DEVNULL) --->>> Saying python to not to throw an error .
print(p1.stderr)

                        and
                        
O/P of an one command is equal to the INPUT of and another command

p1=subprocess.run(['cat','text.txt'],capture_output=True,test=True) --->>> CAT command 
print(p1.stdout) 


p2=subprocess.run(['grep','-n','Gautham'],capture_output=True,test=True,input=p1.stdout) --->>> GREP command to search for a string given
print(p2.stdout) 

Now here in the above code ***** input=p1.stdout ***** is given such that O/P of the command will be the I/P of another command.
'''



# subprocess.call("ls","/Users/gautham/",shell=True) #Same as os.system
# print(os.getcwd())

# op = subprocess.check_output('ls',shell=True,universal_newlines=True)
# print(os.getcwd())
# print(op)


# subprocess.Popen("ls",cwd="/Users/gautham/")
# print(os.getcwd())



# x_1 = str(subprocess.run("pwd",shell=True,cwd="/Users/gautham/Documents/Image-Line/",capture_output=True))
# print(x_1)
# x2 = x_1

# print(x2)

#subprocess.run("ls; cp -r * /Users/gautham/Desktop/",capture_output=True,shell=True,cwd="/Users/gautham/Documents/")
#print(os.getcwd())


# op = subprocess.check_output('ls',shell=True,text=True)
# print(op)

