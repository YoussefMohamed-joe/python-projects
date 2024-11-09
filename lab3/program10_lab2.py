message6=input("please enter your message: ")
result = ""
capitalize_next = False
for i in message6:
    if i == " ":
        result += i
        capitalize_next = True 
    elif capitalize_next:
        result += i.upper() 
        capitalize_next = False
    else:
        result += i.lower()

print(result)