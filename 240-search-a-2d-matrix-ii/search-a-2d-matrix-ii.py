class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums,target):
            l,r=0,len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return False
        res = False
        for i in matrix:
            res = res or binarySearch(i,target)
        return res