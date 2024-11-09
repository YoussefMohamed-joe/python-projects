num=input("please enter your number: ")
if (num.isdigit()):
    num=int(num)
    factorial=1
    while num>0:
        factorial*=num
        num-=1
    print(factorial)
else:
    print("please enter a valid number")