class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_s = 0
        total = sum(nums)

        for i in range(len(nums)):
            if l_s == total-l_s-nums[i]:
                return i
            l_s +=nums[i]

        return -1
        