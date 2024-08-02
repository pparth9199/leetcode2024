class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        for i,n in enumerate(nums):
            if target-n not in cache:
                cache[n]=i
            else:
                return [i,cache[target-n]]