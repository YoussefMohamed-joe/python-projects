num=input("please enter your number: ")

if (num.isdigit()):
    num=int(num)
    i=1
    result=""
    result+="["
    while i<=num:
        result+="["
        j=1
        while j<=i:
            result+=f"{j*i},"
            j+=1
        result=result.rstrip(",")
        result+="],"
        i+=1
    result=result.rstrip(", ")
    result+="]"
    print(result)
else:
    print("please enter a valid number")