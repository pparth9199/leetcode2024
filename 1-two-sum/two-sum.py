class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        n=len(nums)
        for index in range(n):
            if target-nums[index] in cache:
                return [index,cache[target-nums[index]]]
            else:
                cache[nums[index]]=index
        return []
            

        