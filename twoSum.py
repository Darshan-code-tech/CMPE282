def twoSum_try(nums,target):
    list1 = []
    i = 0
    j = len(nums)-1
    while i <= j:
        if nums[i] + nums[j] == target:
            list1.append([i,j])
            i += 1
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return list1
nums = [2,3,6,7,11,15]
x = twoSum_try(nums,9)
print(x)