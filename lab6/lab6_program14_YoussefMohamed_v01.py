tup=(1, 2, 3, 4)
l1=[]
for i in tup:
    for j in tup:
        if(i==j):
            continue
        elif(i>j):
            continue
        else:
            tup1=(i,j)
            l1.append(tup1)
print(l1)
