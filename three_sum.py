def threeSumClosest(nums, target):
    d = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                for k in range(len(nums)):
                    if j != k:
                        c = nums[i] + nums[j] + nums[k]
                        if target == c:
                            d = c
                            print("c", c)
                            return d

    
nums = [0,0,0]
target = 1
print(threeSumClosest(nums, target))