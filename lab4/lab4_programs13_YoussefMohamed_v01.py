num=input("please enter your number: ")
if (num.isdigit()):
    num=int(num)
    while num!=1:
        print(num)
        if num%2==0:
            num=num//2       
        else:
            num=num*3+1
    print(1)
else:
    print("please enter a valid number")


    