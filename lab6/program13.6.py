tup=(1,"aef",3.4,5)
l1=[]
i=len(tup)-1
while i>=0:
    l1.append(tup[i])
    i=i-1
tup=tuple(l1)
print(tup)
