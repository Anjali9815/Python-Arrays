n = -1

def twoSum(nums, target):
    if len(nums) > 2:
        my_dict = {}
        for i in enumerate(nums):
            c = target - i[1]
            if c in nums:
                d = nums.index(c)
                if d != i[0]:
                    print(i[0], d)
                    break
    return "f"
            
# nums = [-3,4,3,90]
nums = [3,2,3]
target = 6
print(twoSum(nums, target))
