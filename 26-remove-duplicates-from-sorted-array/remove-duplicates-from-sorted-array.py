class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        for i in range(len(nums)):
            if nums[i] in seen:
                nums[i]=inf
            else:
                seen.append(nums[i])
        nums = nums.sort()
        return(len(seen))
        