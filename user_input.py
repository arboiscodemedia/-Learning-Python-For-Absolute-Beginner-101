value1 = input("Please enter first integer: \n")
value2 = input("Please enter second integer: \n")

v1 = int(value1)
v2 = int(value2)

choice = input("Enter 1 for addition. \n Enter 2 for subtaction \n Enter 3 for multiplication \n")
choice = int(choice)

if choice == 1:
    print(f'You entered {v1} and {v2} and their addition result is {v1 + v2}')
elif choice == 2:
    print(f'You entered {v1} and {v2} and their difference result is {v1 - v2}')
elif choice == 3:
    print(f'You entered {v1} and {v2} and their product result is {v1 * v2}')
else:
    print("Wrong Choice,Terminating the program")

 