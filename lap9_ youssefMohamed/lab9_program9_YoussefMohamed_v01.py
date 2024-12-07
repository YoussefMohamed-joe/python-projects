def count_inversions(nums):
    myList=[]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
               myList.append((nums[i], nums[j])) 
    return myList





nums = [2, 4, 1, 3, 5]
print(count_inversions(nums))