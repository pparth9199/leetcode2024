class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        curr_sum = 0
        sum_map = {0: 1}  # Initialize the sum map with sum 0 having one count
        
        for num in nums:
            curr_sum += num
            
            # Check if (curr_sum - k) exists in sum_map
            if (curr_sum - k) in sum_map:
                count += sum_map[curr_sum - k]
            
            # Update the sum_map with the current cumulative sum
            if curr_sum in sum_map:
                sum_map[curr_sum] += 1
            else:
                sum_map[curr_sum] = 1
        
        return count