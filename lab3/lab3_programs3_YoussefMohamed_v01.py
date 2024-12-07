length=input("please enter your length: ")
width=input("please enter your width: ")
if length.isdigit() and width.isdigit():
    length=float(length)
    width=float(width)
    area=length*width
    circumference=2*(length+width)
    print(area)
    print(circumference)
elif (not length.isdigit()):
    print("please enter a valid length")
elif (not width.isdigit()):
    print("please enter a valid width")