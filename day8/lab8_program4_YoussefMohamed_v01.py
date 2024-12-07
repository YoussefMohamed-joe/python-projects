employees = {
"Alice": 1200,
"Bob": 800,
"Charlie": 400,
"Diana": 1500,
"Eve": 300
}

sum=0

for sales in employees.values():
    sum+=sales
print(sum)

top=0

for sales in employees.values():
    if sales>top:
        top=sales
for sales in employees:
    if employees[sales]==top:
        print (sales)

newDict={}
l=[]
for sales in employees:
    if employees[sales]>=1000:
        l.append(sales)
else:
    newDict["excellent"]=l

l=[]
for sales in employees:
    if employees[sales]>=500 and employees[sales]<900:
        l.append(sales)
else:
    newDict["Good"]=l

l=[]
for sales in employees:
    if employees[sales]<500:
        l.append(sales)
else:
    newDict["Needs Improvement"]=l
print(newDict)
