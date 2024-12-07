tup=((1, 2), (3, 4), (5, 6))
l=[]
for i in tup:
    for j in i:
        l.append(j)
tup2=tuple(l)
print(tup2)