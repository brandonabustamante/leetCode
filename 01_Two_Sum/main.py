

def twoSum(nums, target):
    
    
    # indexes = []

    # for i in range(0, len(nums)):
    #     cur_val = target - nums[i]
    #     for j in range(i + 1, len(nums)):
    #         if cur_val - nums[j] == 0:
    #             indexes.append(i)
    #             indexes.append(j)

    # return indexes

    num_values = {}

    for index, value in enumerate(nums):
        if target - value in num_values:
            return [num_values[target - value], index]
        else:
            num_values[value] = index


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, 9))