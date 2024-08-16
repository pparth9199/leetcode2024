class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r=0,0
        maxOnes = 0
        if 1 not in nums:
            return 0
        while r<len(nums):
            if nums[r]!=1:
                while r<len(nums) and nums[r]!=1:
                    r+=1
                l=r
            else:
                maxOnes=max(maxOnes,r-l+1)
                r+=1
        return maxOnes