tup=(10, -20, 30, 40, 50)
min=0
max=0
for i in range(0,len(tup)):
    if min>tup[i]:
        min=tup[i]
    if max<tup[i]:
        max=tup[i]
print(min,max)