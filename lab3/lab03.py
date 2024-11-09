# 1
userAge=input("please enter your age: ")
if (userAge.isdigit()):
    userAge=int(userAge)
    print(userAge*10)
else:
    print("please enter a number")

print("=====================================")

# 2

num1=input("please enter your first number: ")
num2=input("please enter your second number: ")
if (num1.isdigit() and num2.isdigit()):
    num4=int(num1)
    num5=int(num2)
    print(num1*num2)
else:
    print("please enter a valid number")

print("=====================================")

# 3

length=input("please enter your length: ")
width=input("please enter your width: ")
if (length.isdigit() and width.isdigit()):
    length=float(length)
    width=float(width)
    area=length*width
    circumference=2*(length+width)
    print(area)
    print(circumference)
elif (not length.isdigit()):
    print("please enter a valid length")
elif (not width.isdigit()):
    print("please enter a valid width")

print("=====================================")

# 4
username= "      Mohamed          Ahmed           "

# 4.a
username=username.replace(" ","")

# 4.B
username=username.strip()

# 4.C


print("=====================================")

# 5

message1=input("please enter your message: ")

reversed=""
for i in message1:
    reversed=i+reversed

print(reversed)

print("=====================================")

# 6

message2=input("please enter your message: ")
counter=0
for i in message2:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        counter+=1

print(counter)

print("=====================================")

# 7

num3=input("please enter your number: ")
if (num3.isdigit()):
    num3=int(num3)
else:
    print("please enter a valid number")
message3=input("please enter your message: ")
print(num3*message3)

print("=====================================")

# 8
message4=input("please enter your message: ")
for i in message4:
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        message4=message4.replace(i,"")
print(message4)

print("=====================================")

# 9
message5=input("please enter your message: ")
char=input("please enter your character: ")
counter2=0
for i in message5:
    if (i==char):
        counter2+=1
print(counter2)

print("=====================================")

# 10

message6=input("please enter your message: ")
capitalize_next=True
for i in message6:
    if(i==" "):
        capitalize_next = True 
    elif capitalize_next:
            message6=message6.replace(i,i.upper(),1)
            capitalize_next = False 
print(message6) 
print("=====================================")

# 11
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