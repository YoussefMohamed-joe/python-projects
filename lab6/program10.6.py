num=input("please enter your number: ")
l1=[]
if(num.isdigit()):
    num=int(num)
    for i in range(1,num+1):
        l2=[]
        for j in range(1,i+1):
            l2.append(j*i)
        l1.append(l2)
    print(l1)

else:
    print("please enter a valid number")