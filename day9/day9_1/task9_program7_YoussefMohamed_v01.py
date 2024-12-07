import random
wordList=["flower","flow","flight","work"]
index= random.randrange(len(wordList)-1)

solve=[]
counter=0
for i in wordList[index]:
    solve.append("_")
print(" ".join(solve))
while counter <= 7:
    guess=input("please enter your guess: ")
    guess=guess.lower()
    if guess in wordList[index]:
        for i in range(len(wordList[index])):
            if guess==wordList[index][i]:
                solve[i]=guess
        print(" ".join(solve))
        if "_" not in solve:
            print("you won")
            break
    else:
        print("Wrong")
        if counter==7:
            break
        print(f"you have {7-counter} tries left")
        print(" ".join(solve))
        counter+=1
if counter==7:
    print("you lost")
