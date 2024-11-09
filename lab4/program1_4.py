message=input("please enter your message: ")
counter=len(message)-1
result=""
while counter>=0:
    result+=message[counter]
    counter-=1
print(result)