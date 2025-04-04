class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i,v in enumerate(nums):
            if target-v in cache:
                return [i,cache[target-v]]
            else:
                cache[v] = i