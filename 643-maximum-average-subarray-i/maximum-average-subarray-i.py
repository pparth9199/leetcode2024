class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left,right=0,0
        res=0
        summ=0
        max_sum=float('-inf')
        while right < len(nums):
            summ+=nums[right]

            if right-left>=k:
                summ-=nums[left]
                left+=1
            if right-left>=k-1:
                max_sum=max(max_sum,summ/k)
            
            right+=1
        return max_sum