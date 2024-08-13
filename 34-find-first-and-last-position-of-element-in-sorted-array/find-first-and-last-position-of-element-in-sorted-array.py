class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums,target,is_left):
            left=0
            right = len(nums)-1
            idx = -1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>target:
                    right = mid-1
                elif nums[mid]<target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_left:
                        right = mid-1
                    else:
                        left=mid+1

            return idx

        left=binarySearch(nums,target,True)
        right=binarySearch(nums,target,False)

        return [left,right]