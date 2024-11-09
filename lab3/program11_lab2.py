message7=input("please enter your message: ")
capitalize_next=True
for i in message7:
    if(capitalize_next):
        message7=message7.replace(i,i.lower(),1)
        capitalize_next = False 
    else:
            message7=message7.replace(i,i.upper(),1)
            capitalize_next = True 
print(message7) 