class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= max(nums)
        if len(nums)-1==n:
            return n+1
        l = len(nums)
        
        s=(n*(n+1))//2
        return s-sum(nums)
