data = (12, 45, 78, 23, 56, 89, 100, 34, 67, 90)
l=list(data)


n = len(l)
buckets = [[] for _ in range(n)]

for num in l:
    bi = int(n * num)
    buckets[bi].append(num)

   
for bucket in buckets:
    for i in range(1, len(bucket)):
        num = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > num:
            l[j + 1] = bucket[j]
            j -= 1
        l[j + 1] = num

   
index = 0
for bucket in buckets:
    for num in bucket:
        l[index] = num
        index += 1

data=tuple(l)
print(data)