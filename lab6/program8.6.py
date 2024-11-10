sum=0
for i in range(1,51):
    if(i%2==1):
        sum=sum+i
print(sum)




sum=0
i=1
while i<=50:
    if(i%2==1):
        sum=sum+i
    i=i+1
print(sum)


sum=0
i=1
l1=[]
while i<=50:
    if(i%2==1):
        l1.append(i)
    i=i+1
i=0
while i<len(l1):
    sum=sum+l1[i]
    i=i+1
print(sum)