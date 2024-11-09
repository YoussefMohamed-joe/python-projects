message4=input("please enter your message: ")
for i in message4:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        message4=message4.replace(i,"")
print(message4)