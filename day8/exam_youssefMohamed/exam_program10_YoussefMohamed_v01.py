nested_tuple = (1, 2, (3, 4), (5, 6, (7, 8)))
l = []

for i in nested_tuple:
    if isinstance(i, tuple):
        for j in i:
            if isinstance(j, tuple):
                for k in j:
                    l.append(k)
            else:
                l.append(j)
    else:
        l.append(i)

new_tuple = tuple(l)
print(new_tuple)