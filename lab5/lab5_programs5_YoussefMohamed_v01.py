message=input("please enter your message: ")
messageList=list(message)
i=0
while i < len(messageList):
    if messageList[i] in "aeiou":
        messageList.pop(i)
        i-=1
    i+=1

print("".join(messageList))