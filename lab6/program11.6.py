num=input("please enter your number: ")
if(num.isdigit()):
    num=int(num)
    for i in range(1,num+1):
        print(" "*(num-i)+"*"*i)

else:
    print("please enter a valid number")