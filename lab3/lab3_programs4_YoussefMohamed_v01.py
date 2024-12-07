username= "      Mohamed          Ahmed           "


print(username)
# 4.C

result=""
preChar=""
for i in username:
    if (i!=" "):
        result+=i
        preChar=i
    else:
        if preChar!=" ":
            result+=" "
        preChar=i
result=result.strip()
print(result)