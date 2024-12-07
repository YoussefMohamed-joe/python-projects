num=input("please enter your number: ")
if (num.isdigit()):
    num=int(num)
    if num==0:
        print("neither odd nor even")
    elif num%2==0:
        print("even")
    else:
        print("odd")
else:
    print("please enter a valid number")