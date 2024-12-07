def array(length,start):
    l=[]
    counter=0
    while counter<length:
        l.append(start)
        start+=1
        counter+=1
    return l

length=input("please enter your length: ")
start=input("please enter your start: ")
if(length.isdigit() and start.isdigit()):
    length=int(length)
    start=int(start)
    print(array(length,start))
else:
    print("please enter a valid number")