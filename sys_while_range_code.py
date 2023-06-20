import os
import sys

def num_ran():
    while True:
        try:
            num = int(input("Enter the num : "))
        except ValueError:
            print("Please enter a valid integer")
        else:
            if num in range(6):
                print(f"Thanks for entering {num}")
                break
            else:
                print("Please enter a value between 0 and 5")

number = "y"
while(number.lower() == "y"):
    num_ran()
    number = input("Do you wanna try again : ?  [ Please enter Y to continue :  ]")
#print("Thank you")
sys.exit("Thank you")