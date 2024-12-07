dect={
    "name":"youssef",
    "age":"22",
    "track":"iti45",
    "city":"cairo",
    "email":"mohammedyoussef111@gmail.com"
}


dectasc={}
dectDesc={}


l1=[]
for key in dect.values():
    l1.append(key)

l1.sort()
for i in l1:
    for key in dect:
        if dect[key]==i:
            dectasc[key]=i
            break

l2=[]
for key in dect.values():
    l2.append(key)

l2.sort(reverse=True)
for i in l2:
    for key in dect:
        if dect[key]==i:
            dectDesc[key]=i
            break

print(dectasc)
print(dectDesc)