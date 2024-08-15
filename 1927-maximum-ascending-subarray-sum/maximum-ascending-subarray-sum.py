class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        l,r=0,0
        currentSum=0
        while r<len(nums):
            if r>0 and nums[r]<=nums[r-1]:
                currentSum =0
                l=r
            currentSum = sum(nums[l:r+1])
            maxSum=max(currentSum,maxSum)
            r+=1
        return maxSum
            