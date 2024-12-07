message=input("please enter your message: ")
result=""
message=message.strip()
result+=message[0].upper()
result+=message[1].lower()
counter=1
while counter<len(message) :  
    if counter == len(message)-1:
        break 
    if message[counter]==" ":
        result+=message[counter+1].upper()
        counter+=1
    else:
        result+=message[counter+1].lower()
        counter+=1
print(result)
