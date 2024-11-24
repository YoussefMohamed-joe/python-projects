def top_k_frequent(nums, k):
    dect = {}
    for i in nums:
        if i not in dect:
            dect[i] = 1
        else:
            dect[i] += 1
    result=[]
    for i in dect:
        if dect[i] >= k:
            result.append(i)
    result.sort()
    return result

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))