userAge=input("please enter your age: ")
if (userAge.isdigit()):
    userAge=int(userAge)
    print(userAge*10)
else:
    print("please enter a number")

print("=====================================")