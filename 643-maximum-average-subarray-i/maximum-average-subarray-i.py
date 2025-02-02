class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==1:
            return nums[0]
        if len(nums)==k:
            return sum(nums)/k
        s=sum(nums[:k])
        maxAvg = s
        for i in range(k,len(nums)):
            s-=nums[i-k]
            s+=nums[i]
            maxAvg = max(maxAvg,s)
        return maxAvg/k
