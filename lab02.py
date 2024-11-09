# 1
firstName=input("enter your first name: ")
lastName=input("enter your last name: ")
age=int(input("enter your age: "))
print ("My name is {} {} and my age is {} ".format(firstName,lastName,age)) 

print("=====================================")

# 2
print(type(firstName))
print(type(lastName))
print(type(age))

print("=====================================")

# 3
message1=input("please enter your message: ")
print(message1)

print("=====================================")

# 4
salary1=float(input("please enter your salary: "))
print(salary1)
print(type(salary1))

print("=====================================")

# 5
message2=input("please enter your message: ")
print(message2[::-1])

print("=====================================")

# 6
print(len(message2))

print("=====================================")

# 7.1
print(message2.count("i"))

print("=====================================")

# 7.2
num1=int(input("please enter your number: "))
if (num1>0):
    print("positive")
elif (num1<0):
    print("negative")
else:
    print("zero")

print("=====================================")

# 8
num2=int(input("please enter your first number: "))
num3=int(input("please enter your second number: "))
print(num2+num3)
print(num2-num3)
print(num2*num3)
print(num2/num3)

print("=====================================")

# 9
dayName=input("please enter your day name: ")
if (dayName=="Sunday" or dayName=="sunday"):
    print("whish you a good week")
elif(dayName=="Tuesday" or dayName=="tuesday"):
    print("The weekend is near")
elif(dayName=="Friday" or dayName=="friday"):
    print("enjoy your weekend")
elif(dayName=="Saturday" or dayName=="saturday" or dayName=="monday" or dayName=="monday"or dayName=="wednesday" or dayName=="wednesday"or dayName=="thursday" or dayName=="thursday"):
    print("ma3lsh")
else:
    print("have a good day")

print("=====================================")

# 10
userAge=int(input("please enter your age: "))
if (type(userAge)==int):
    print(age*10)
else:
    print("please enter a number")

print("=====================================")

# 11
num4=int(input("please enter your first number: "))
num5=int(input("please enter your second number: "))
if (type(num4)==int and type(num5)==int):
    print(num4*num5)
else:
    print("please enter a number")

print("=====================================")

# 12
length=int(input("please enter your length: "))
width=int(input("please enter your width: "))
area=length*width
circumference=2*(length+width)
print(area)
print(circumference)