class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        l = 0
        h = len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if nums[l] < nums[mid] and nums[l] < nums[h]:
                h = mid - 1
            elif nums[h] < nums[l] and nums[h] < nums[mid]:
                l = mid + 1
            elif nums[mid] < nums[l] and nums[mid] < nums[h]:
                l += 1
                h -= 1
            else:
                return nums[mid]
        