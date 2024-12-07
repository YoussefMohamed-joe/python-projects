num=input("please enter your number: ")
if (num.isdigit()):
    num=int(num)
    i=1
    while i<=num:
        print(" "*(num-i),end="")
        print("*"*i)
        i+=1
else:
    print("please enter a valid number")