class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checker = set()
        for i in nums:
            checker.add(i)
        return len(checker)!=len(nums)