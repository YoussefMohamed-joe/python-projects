num=input("please enter your positive integer number: ")

while not num.isdigit():
    print("please enter a valid number")
    num=input("please enter your positive integer number: ")

num=int(num)
print(num)


