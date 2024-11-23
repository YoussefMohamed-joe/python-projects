message=input("please enter your message: ")
result="" 
counterChar=""
for i in message:
    counter=0
    if i not in counterChar:
        for j in message:
            if j==i:
                counter+=1
            
        counterChar+=i
        result+=f"{i}-->{counter},"
print(result)
