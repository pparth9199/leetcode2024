class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        for index, value in enumerate(nums):
            if target-value in cache:
                return [index,cache[target-value]]
            else:
                cache[value]=index
        return []
            

        