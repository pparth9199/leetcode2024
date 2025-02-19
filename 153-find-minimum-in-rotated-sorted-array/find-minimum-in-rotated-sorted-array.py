class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-1
        if len(nums)<2:
            return nums[0]

        while lo<=hi:
            mid = (lo+hi)//2
            if mid!=0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]>nums[hi]:
                lo=mid+1
            elif mid==0 and nums[mid+1]>nums[mid]:
                return nums[0]
            else:
                hi=mid-1
    