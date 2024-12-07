def checkNumber(num):
    if num.isdigit():
        num=int(num)
        if num%5==0 and num%3==0:
            return "Fizzbuzz"
        elif num%5==0:
            return "buzz"
        elif num%3==0:
            return "fizz"
        else:
            return "not divisible by 3 or 5"
    else:
        return "please enter a valid number"

num1=input("please enter your number: ")
print(checkNumber(num1))