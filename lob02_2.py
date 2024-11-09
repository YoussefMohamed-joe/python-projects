num4=input("please enter your first number: ")
num5=input("please enter your second number: ")
if (num4.isdigit() and num5.isdigit()):
    num4=int(num4)
    num5=int(num5)
    print(num4*num5)
else:
    print("please enter a valid number")