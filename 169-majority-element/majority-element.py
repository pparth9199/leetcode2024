class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i , j in enumerate(nums):
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1
        maximum = 1
        majority = nums[0]
        for i in d.keys():
            if d[i] > maximum:
                maximum = d[i]
                majority = i
        return majority