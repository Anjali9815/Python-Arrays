nums = [1,7,3,6,5,6]


total = sum(nums)
sum = 0

for i in nums:
    if sum == total - nums[i]:
        print(i)
        break

