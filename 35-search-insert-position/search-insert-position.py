class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:  # Target found
                return mid
            elif nums[mid] < target:  # Search right half
                left = mid + 1
            else:  # Search left half
                right = mid - 1
        
        # If not found, `left` is the insertion index
        return left
        