num1=input("please enter your first number: ")
num2=input("please enter your second number: ")
operation=input("please enter your operation: ")
operation=operation.lower()
if (num1.isdigit() and num2.isdigit()):
    num1=int(num1)
    num2=int(num2)
    if (operation=="add"):
        print(num1+num2)
    elif (operation=="subtract"):
        print(num1-num2)
    elif (operation=="multiply"):
        print(num1*num2)
    elif (operation=="division"):
        print(num1/num2)
    else:
        print("please enter a valid operation")
else:
    print("please enter a valid number")