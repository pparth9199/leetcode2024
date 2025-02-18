class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        l = 0
        h = len(nums) - 1
        while (l<=h):
            mid =(l+h)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1      
        return -1