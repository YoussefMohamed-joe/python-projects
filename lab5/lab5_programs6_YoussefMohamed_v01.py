message=input("please enter your message: ")
messageList=list(message)
counter =1
while counter<len(messageList):
    messageList.insert(counter,"i")
    counter+=2

print("".join(messageList))
