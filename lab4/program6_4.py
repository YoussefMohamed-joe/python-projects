num=input("please enter your number: ")
if (num.isdigit()):
    num=int(num)
    while num>=0:
        print(num)
        num-=1
else:
    print("please enter a valid number")
