try:
    l1=[]
    for i in range(1,6):
        num=input(f"please enter your {i} element: ")
        l1.append(num)
    print(l1)
except ValueError:
    print("please enter a valid number")

