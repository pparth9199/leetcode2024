class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr,target):
            l,r=0,len(arr)-1

            while l<=r:
                mid = (l+r)//2

                if arr[mid]==target:
                    return True
                elif arr[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return False

        res=False
        for i in range(len(matrix)):
            res = res or binarySearch(matrix[i],target)

        return res
