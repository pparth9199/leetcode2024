class Solution:
    def findMin(self, nums: List[int]) -> int:
        currentMin = 1001
        l=0
        r=len(nums)-1

        while l<=r:
            print(l,r)
            mid = (l+r)//2
            currentMin = min(currentMin,nums[mid])
            if nums[r]<=nums[mid]:
                l=mid+1
            elif nums[r]>nums[mid]:
                r=mid-1
            elif nums[l]<=nums[mid]:
                r=mid-1
            else:
                l=mid+1

        return currentMin