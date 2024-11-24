def top(message):
    words=list(message.split(" "))
    dect={}
    for i in words:
        if i not in dect:
            dect[i]=1
        else:
            dect[i]+=1
    l=list(dect.values())
    l.sort(reverse=True)
    newdect={}
    for i in l:
        for key in dect:
            if dect[key]==i:
                newdect[key]=i
    return newdect

message=input("please enter your message: ")   
print(top(message))