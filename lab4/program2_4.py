message=input("please enter your message: ")
counter=0
result=0
while  counter<len(message):
    if message[counter] in"aeiou":
        result+=1
    counter+=1
print(f"there are {result} vowels in your message")