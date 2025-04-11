class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_map = {0: -1}  
        max_len = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum - k in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum - k])

            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i 

        return max_len