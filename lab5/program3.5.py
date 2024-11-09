myList=[]
counter=1
while counter<=5:
    message=input(f"please enter your {counter} word: ")
    myList.append(message)
    counter+=1
myList.sort(reverse=True)
print(myList)
myList.sort()
print(myList)