file=open("1.txt")
result=""

counter=0
for line in file:
    counter+=1
    if counter==2:
        result=line

print(result)

