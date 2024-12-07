num=input("please enter your number: ")
if (num.isdigit()):
    num=int(num)
    result=""
    for i in range(num,-2,-1):
        result+=f"{i},"
    print(result.rstrip(","))
else:
    print("please enter a valid number")