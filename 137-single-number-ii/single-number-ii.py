class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i in nums:
            if count[i]!=3:
                return i