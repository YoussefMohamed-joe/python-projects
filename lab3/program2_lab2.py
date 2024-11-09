num1=input("please enter your first number: ")
num2=input("please enter your second number: ")
if num1.isdigit() and num2.isdigit():
    num4=int(num1)
    num5=int(num2)
    print(num1*num2)
else:
    print("please enter a valid number")