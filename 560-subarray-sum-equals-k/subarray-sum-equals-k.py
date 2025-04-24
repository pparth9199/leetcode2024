class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = {0:1}
        count = 0
        current_sum = 0

        for num in nums:
            current_sum+=num
            diff = current_sum-k
            if diff in sum_count:
                count+=sum_count[diff]
            if current_sum in sum_count:
                sum_count[current_sum] += 1
            else:
                sum_count[current_sum] = 1
        return count