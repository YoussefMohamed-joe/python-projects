message=input("please enter your message: ")
result=[]
i=0
while i < len(message)-2:
    if message[i:i+3] == "iti":
        result.append("iti")
    i+=1

print(len(result))