word=input("please enter your word: ")
revWord=word[::-1]
length=int(len(word)/2)
for i in range(length):
    if word[i]==revWord[i]:
        print("the word is palindrome")
        break
else:
    print("the word is not palindrome")