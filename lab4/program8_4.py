num=input("please enter your number: ")
if (num.isdigit()):
    num=int(num)
    result="output "
    while num>=1:
        result+=f"{num}, "
        num-=1 
    print(result.rstrip(", "))
else:
    print("please enter a valid number")

    