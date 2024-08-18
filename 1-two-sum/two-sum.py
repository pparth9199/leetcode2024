class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for n,i in enumerate(nums):
            if target-i in cache:
                return [n,cache[target-i]]
            cache[i]=n
        return [-1,-1]