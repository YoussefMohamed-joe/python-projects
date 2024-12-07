def largest_number(nums):
    strNums=[]
    for i in nums:
        strNums.append(str(i))
    for i in range(len(strNums)):
        for j in range(i + 1, len(strNums)):
            if strNums[i] + strNums[j] < strNums[j] + strNums[i]:
                strNums[i],strNums[j]= strNums[j] ,strNums[i]
                
    return int("".join(strNums))

nums = [3, 30, 34, 5, 9]
print(largest_number(nums))