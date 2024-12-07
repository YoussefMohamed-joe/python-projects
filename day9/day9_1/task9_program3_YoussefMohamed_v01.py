def reverseString(message):
    reversed = ""
    for i in message:
        reversed = i + reversed
    return reversed

message = input("Please enter your message: ")
print(reverseString(message))