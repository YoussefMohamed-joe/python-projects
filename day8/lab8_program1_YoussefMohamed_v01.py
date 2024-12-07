grades = [45, 78, 88, 34, 90, 67, 55, 39, 100, 62]

max=0
min=0
total=0
average=0

for i in grades:
    total=total+i
    if max<i:
        max=i
    if min==0 or min>i:
        min=i

average=total/len(grades)

print("The highest grade is",max)
print("The lowest grade is",min)
print("The average grade is",average)
print("The total grade is",total)