for i in range(2,21):
    if(i%2==0):
        print(i,end=" ")
print()
l1=[]
i=2
while i <=20:
    if(i%2==0):
        l1.append(i)
    i=i+1
tup=tuple(l1)
print(tup)
print(l1)