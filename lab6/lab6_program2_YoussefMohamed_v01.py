i=1
l1=[]
sum=0
while i<=10:
    number=input(f"Enter your {i} number:")
    if(number.isdigit()):
        i=i+1
        number=int(number)
        sum=sum+number
        l1.append(number)       
    else:
        print("Enter a valid number")
tup=tuple(l1)
print(tup)
print(sum)