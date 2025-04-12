class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right=0,0
        min_size = float('inf')

        summ = 0

        while right<len(nums):
            summ+=nums[right]
            while summ>=target:
                min_size = min(min_size,right-left+1)
                summ-=nums[left]
                left+=1
                
            right+=1
        return min_size if min_size<inf else 0
        


