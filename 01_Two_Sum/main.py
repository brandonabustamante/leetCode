

def twoSum(nums, target):
    
    indexes = []

    for i in range(0, len(nums)):
        cur_val = target - nums[i]
        for j in range(i + 1, len(nums)):
            if cur_val - nums[j] == 0:
                indexes.append(i)
                indexes.append(j)

    return indexes







nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, 9))