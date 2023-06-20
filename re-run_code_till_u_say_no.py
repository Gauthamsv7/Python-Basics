


def hrs_to_sec(hrs,min,sec):
    return hrs*3600+min*60+sec

print("welcome to the time converter")

count = "y"
while(count.lower()=="y"):
    hrs = int(input("Enter the no of hrs : "))
    min = int(input("Enter the no of min : "))
    sec = int(input("Enter the no of sec : "))
    #print("That's {} secs".format(hrs_to_sec(hrs,min,sec)))
    print(f"That's {(hrs_to_sec(hrs,min,sec))} seconds \n")
    count = input("Do you want to try another conversion ? [ Y to continue : ]")
    
print("Good Bye !")
    