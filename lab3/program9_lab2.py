message5=input("please enter your message: ")
result = ""  
countedChars = "" 

for i in message5:
        if i not in countedChars: 
            count = 0
            for j in message5: 
                if j == i:
                    count += 1
            
            countedChars += i 
            result += f"{i} --> {count}, "  
print(result.rstrip(", "))

