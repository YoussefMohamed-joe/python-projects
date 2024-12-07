message2=input("please enter your message: ")
counter=0
for i in message2:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        counter+=1

print(counter)