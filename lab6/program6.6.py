myL=[]
for i in range(0,51,5):
    myL.append(i)
myL.remove(0)
print(myL,end=" ")

print()

myL1=[]
for i in range(1,51):
    if(i%5==0):
        myL1.append(i)
print(myL1,end=" ")

print()

myL2=[]
i=1
while i<=50:
    if(i%5==0):
        myL2.append(i)
    i=i+1
print(myL2)
