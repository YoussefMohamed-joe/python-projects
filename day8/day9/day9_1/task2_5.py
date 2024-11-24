def lognestSub(message):
    longest = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in message:
        for j in alpha:
            if i == j:
                longest += i
                for k in range(alpha.index(i), -1,-1):
                    alpha = alpha.replace(alpha[k], "")
    return longest



message = input("Please enter your message: ")
print(lognestSub(message))