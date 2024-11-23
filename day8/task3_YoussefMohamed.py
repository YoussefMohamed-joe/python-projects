data = (12, 45, 78, 23, 56, 89, 100, 34, 67, 90)
newData=()
counter=0
for num in data:
    if(counter<3):
        newData+=(num,)   
    if(counter>len(data)-3):
        newData+=(num,)
    counter+=1
print(newData)
print()

#####################
sum=0
for num in data:
    sum+=num
print(sum)

#####################
num=input("please enter your number: ")
exists=False
if (num.isdigit()):
    num=int(num)
    for i in data:
        if(i==num):
            exists=True
            break
    if(exists):
        print("the number is in the tuple")
    else:
        print("the number is not in the tuple")
else:
    print("please enter a valid number")

#####################
l=[]
for i in data:
    l.append(i)
l.append(102)
data=tuple(l)
print(data)

#####################
l=[]
for i in data:
    l.append(i)
l.sort()
data=tuple(l)
print(data)