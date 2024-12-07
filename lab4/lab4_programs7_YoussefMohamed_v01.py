num=input("please enter your number: ")
if (num.isdigit()):
    num=int(num)
    sum=0
    while num>=0:
        if num%2==0:
            sum+=num
        num-=1
    print(sum)
else:
    print("please enter a valid number")


