class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize two pointers
        left = 1  # This will point to the position where the next unique element should be placed
        
        # Iterate through the array starting from the second element
        for right in range(1, len(nums)):
            # If the current element is not equal to the previous one, it is unique
            if nums[right] != nums[right - 1]:
                # Place the unique element at the left pointer's position
                nums[left] = nums[right]
                left += 1  # Move the left pointer to the next position
                
        # The value of `left` will be the count of unique elements
        return left
        