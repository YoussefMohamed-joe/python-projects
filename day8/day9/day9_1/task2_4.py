import re

def validName(name):
    name=name.strip()
    if name.isalpha():
        if len(name)>0:
            return name
        else:
            return "please enter a valid name"
    else:
        return "please enter a valid name"
    
def validEmail(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return email
    else:
        return "please enter a valid email"
    
name=input("please enter your name: ")
email=input("please enter your email: ")
print(validName(name))
print(validEmail(email))