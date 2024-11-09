message=input("please enter your message: ")
messageList=list(message)
counter =0
i=0
while i < len(messageList):
    if messageList[i] in "aeiou":
        counter+=1
    i+=1

print(counter)