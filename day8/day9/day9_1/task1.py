def checkValid(num):
    if num.isdigit():
        return num
    else:
        return "please enter a valid number"

num=input("please enter your number: ")
print(checkValid(num))