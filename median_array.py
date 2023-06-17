

def findMedianSortedArrays(nums1, nums2):
    result = 0
    for i in nums2:
        nums1.append(i)
    nums1.sort()
    print(nums1)
    if len(nums1) % 2 != 0:
        # res = 
        result = nums1[int(len(nums1) / 2)]
    else:
        result = (nums1[int(len(nums1) / 2)] + nums1[(int(len(nums1) / 2)) - 1]) / 2
    print(result)


nums1 = [1,3, 5, 6]
nums2 = [2]


findMedianSortedArrays(nums1, nums2)
