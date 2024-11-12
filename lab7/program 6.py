dect={
    "name":"youssef",
    "age":22,
    "track":"iti45",
    "city":"cairo",
    "email":"mohammedyoussef111@gmail.com"
}

dectTemp={}
for key in dect:
    dectTemp[dect[key]]=key
dect=dectTemp
print(dect)