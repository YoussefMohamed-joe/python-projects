my_dict = {"a": 3, "b": 1, "c": 2}
l=list(my_dict.values())
new_dict={}
l.sort()
for i in l:
    for key in my_dict:
        if my_dict[key]==i:
            new_dict[key]=i
print(new_dict)
