class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        def rowSearch(nums):
            l,r=0,len(nums)-1
            print(nums)
            while l<=r:
                mid = (l+r)//2
                print(mid)
                if nums[mid]==target:
                    return True
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1

            return False

        l,r=0,len(matrix)-1

        while l<=r:
            mid=(l+r)//2

            if matrix[mid][0]>target:
                r=mid-1
            elif matrix[mid][0]<=target and matrix[mid][-1]>=target:
                return rowSearch(matrix[mid])
            else:
                l=mid+1
        return False