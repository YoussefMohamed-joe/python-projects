num=input("please enter your number: ")
l1=[]
if (num.isdigit()):
    num=int(num)
    i=1
    while i<=num:
        l2=[]
        j=1
        while j<=i:
            l2.append(j*i)
            j+=1
        i+=1
        l1.append(l2)
    print(l1)
else:
    print("please enter a valid number")

