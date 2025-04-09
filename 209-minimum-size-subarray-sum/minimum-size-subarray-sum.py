class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,1
        min_len=float('inf')
        s=0
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                min_len = min(min_len, r - l + 1)
                s -= nums[l]
                l += 1

        return min_len if min_len != float('inf') else 0

