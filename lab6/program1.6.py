myTuple=(10,20,30,40,50)


myTuple1=(myTuple[0],myTuple[1],myTuple[2])
print(myTuple1)


l1=[]
for i in range(0,3):
    l1.append(myTuple[i])
myTuple1=tuple(l1)
print(myTuple1)

l2=[]
counter=0
for i in myTuple:
    if(counter==3):   
        break
    else:
        counter=counter+1   
        l2.append(i) 
myTuple2=tuple(l2)
print(myTuple2)