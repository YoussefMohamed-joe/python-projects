message=input("please enter your message: ")
dect={}
for i in message:
    dect[i]=message.count(i)
print(dect)
    
dect={}
counter=0
for i in message:
    if i not in dect:
        counter=0
        counter+=1
        dect[i]=counter
        
    else:
        counter+=1
        dect[i]=counter

print(dect)