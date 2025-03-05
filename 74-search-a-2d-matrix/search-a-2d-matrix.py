class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums,target):
            l=0
            r=len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return False
        l=0
        h=len(matrix)-1
        while l<=h:
            mid = (l+h)//2
            if matrix[mid][0]<=target and target<=matrix[mid][-1]:
                return binarySearch(matrix[mid],target)
            elif matrix[mid][0]>target:
                h=mid-1
            elif matrix[mid][-1]<target:
                l=mid+1
        return False