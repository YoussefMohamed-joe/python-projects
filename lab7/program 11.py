
l1=[]
for i in range(1,6):
    num=int(input(f"please enter your {i} number: "))
    l1.append(num)

try:
    index=int(input("please enter your index: "))
    if (index>=0 and index<len(l1)):
        print(l1[index])
    else:
        print("the index you entered is out of range.")
except ValueError:
    print("please enter a valid number")