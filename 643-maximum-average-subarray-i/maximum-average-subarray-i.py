class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        best=current = sum(nums[:k])
        
        r=k
        while r<len(nums):
            current+= nums[r]-nums[r-k]
            best = max(best,current)
            r+=1
        return best/k