global grade
def grade():
    global grade
    grade=0
    def ass():
         global grade
         grade=90
    ass()
    return grade

print(grade())