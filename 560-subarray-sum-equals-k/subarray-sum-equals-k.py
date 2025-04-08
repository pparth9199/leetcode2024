class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Initialize with prefix sum 0 and count 1
        
        for num in nums:
            prefix_sum += num 
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]
            prefix_sum_count[prefix_sum] += 1  # Update the frequency if the current prefix_sum
        
        return count