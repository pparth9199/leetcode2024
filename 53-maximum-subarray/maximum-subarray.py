class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        l = 0
        ans = -inf
        for r in range(len(nums)):
            s = s + nums[r]
            ans = max(ans, s)
            if s <= 0:
                s = 0
        return ans
        # c_sum = 0
        # max_sum = -inf

        # for num in nums:
        #     c_sum += num

        #     max_sum = max(c_sum, max_sum)
        #     if c_sum <= 0:
        #         c_sum = 0
            

        # return max_sum