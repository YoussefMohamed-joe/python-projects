num=input("please enter your number: ")
reversed=0
if (num.isdigit()):
    num=int(num)
    while num!=0:
        digit=num%10
        reversed=reversed*10+digit
        num=num//10
    print(reversed)
else:
    print("please enter a valid number")