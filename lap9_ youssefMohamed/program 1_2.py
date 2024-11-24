def checkAni(message1,message2):
    letters1=[]
    letters2=[]
    for i in message1:
        letters1.append(message1.count(i))
    for i in message2:
        letters2.append(message2.count(i))
    letters1.sort()
    letters2.sort()
    if letters1==letters2:
        print("anagram")
    else:
        print("not anagram")
    

message1=input("please enter your message: ")
message2=input("please enter your message: ")
checkAni(message1,message2)