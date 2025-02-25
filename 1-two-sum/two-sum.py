class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, j in enumerate(nums):
            if target - nums[i] in visited:
                return (i, visited[target - nums[i]])
            else:
                visited[j] = i
        