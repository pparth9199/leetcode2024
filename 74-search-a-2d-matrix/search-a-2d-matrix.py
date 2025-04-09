class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        # def rowSearch(nums):
        #     l,r=0,len(nums)-1
        #     print(nums)
        #     while l<=r:
        #         mid = (l+r)//2
        #         print(mid)
        #         if nums[mid]==target:
        #             return True
        #         elif nums[mid]<target:
        #             l=mid+1
        #         else:
        #             r=mid-1

        #     return False

        # l,r=0,len(matrix)-1

        # while l<=r:
        #     mid=(l+r)//2

        #     if matrix[mid][0]>target:
        #         r=mid-1
        #     elif matrix[mid][0]<=target and matrix[mid][-1]>=target:
        #         return rowSearch(matrix[mid])
        #     else:
        #         l=mid+1
        # return False