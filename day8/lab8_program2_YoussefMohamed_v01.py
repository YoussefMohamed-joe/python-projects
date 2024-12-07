students = [
["Alice", 85, 90, 78],
["Bob", 72, 88, 91],
["Charlie", 90, 87, 85],
["Diana", 60, 65, 70]
]
top=0
total=0
counter=0
for student in students:
    for i in student[1:]:
        total+=i

    average=round(total/3,2)
    students[counter].append(average)
    students[counter].append(total)
    if average >= 60 and average < 65:
        students[counter].append("pass")
    elif average >= 65 and average < 75:
        students[counter].append("good")
    elif average >= 75 and average < 85:
        students[counter].append("very good")
    elif average >= 85:
        students[counter].append("excellent")
    counter+=1
    total=0
    if average>top:
        top=average
    

print(students)
#######################
for student in students:
    if student[4]==top:
        print(student)
#######################
nL=[]
for student in students:
    nL.append(student[4])
nL.sort(reverse=True)
print(nL)
tempL=[]
for i in nL:
    for student in students:
        if student[4]==i:
            tempL.append(student)
students=tempL
print(students)
########################

totalClass=0
for student in students:
    totalClass+=student[4]

averageClass=round(totalClass/len(students),2)
print(averageClass)