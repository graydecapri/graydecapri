#Module
import random
import sys
import datetime
    
input("Welcome to the hotel regesteration system!")
print("1.Check in")
print("2.Check out")
print("3.Exit")

while True:  
    c = int(input("Please enter your choice (1-3): "))
    if c in [1,2,3]:
        break
    else:
        print("Invalid input.Please enter the correct input.")
        
#module form       
pc = random.randint(1, 50)
date = datetime.datetime.now()

#Checking in    
if c == 1 :
    input("Welcome to Hotel De La Playa!")
    
    name1 = input("Please,enter your first name: ")
    name2 = input("Now, your last name: ")
    s = input(str("Enter your gender (M/F): ")).upper()
#Gender title system
    if s == "M":
        title = "Mr. "
    elif s == "F":
        title = "Ms. "
    else:
        print("Invalid input. Please enter the correct input.")
        
#Menu
    print()
    print()
    print("         Hotel Menu")
    print()
    print("1. Small room, 1 bed : 40$")
    print("2. Small room, 2 beds : 60$")
    print("3. Medium room, 1 bed : 100$")
    print("4. Medium room, 2 beds : 120$")
    print("5. VIP room : 250$")
    
    while True:
        m = int(input("Enter your choice here: "))
        if m in [1,2,3,4,5]:
            break
        else:
            print("Invalid choice. Please enter the correct input.")
            
    day = int(input("Please enter the amount of day you'll be staying for: "))
    
#Math for p's variable
    if m == 1:
        p = day * 40
    elif m == 2:
        p = day * 60
    elif m == 3:
        p = day * 100
    elif m == 4:
        p = day * 120
    else:
        p = day * 250
                 
#Hotel reciept
    print("")
    input(f"Hello {title}{name2}, Welcome to the Hotel De La Playa!")
    print("Here is your reciept: ")
    print(f"Check in date: {date.strftime("%c")}")
    print("Room rumber:", pc)
    print("Days amount:", day)
    print(f"Overall price: {p}$")
 
#Checking out   
elif c == 2 :
    print("Checking out for you. . .")
    print("Check out date: ", date.strftime('%c'))
    print("Good bye, have a safe travel :)")
    sys.exit()
#Exit
else:
    print("Good bye, hope to see you next time!")
    sys.exit()