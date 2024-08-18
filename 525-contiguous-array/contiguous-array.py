class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        count = 0
        max_len = 0
        count_map = {0: -1}  # Initialize the count map with sum 0 at index -1
        
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            
            if count in count_map:
                max_len = max(max_len, i - count_map[count])
            else:
                count_map[count] = i
        
        return max_len
