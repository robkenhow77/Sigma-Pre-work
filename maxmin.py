nums1 = [2, 4, 1, 0, 2 ,-1]
nums2 = [20, 50, 12, 6, 14, 8]
nums3 = [100, -100]
nums = [nums1, nums2, nums3]


def maxmin(numbers):
    return [sorted(numbers)[0], sorted(numbers)[-1] ]


for i in nums:
    print(maxmin(i))

