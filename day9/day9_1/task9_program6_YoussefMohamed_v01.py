l=[]
def task(num):
    if num.isdigit():
        num=int(num)
        l.append(num)
    else:
        print("please enter a valid number")

def calculate(l):
    sum=0
    for i in l:
        sum=sum+i
    count=len(l)
    average=sum/count
    print(f"your total is {sum},the average is {average} and the count is {count}")




while True:
    num=input("please enter your number: ")
    if num=="done":
        break
    else:
        task(num)

calculate(l)
