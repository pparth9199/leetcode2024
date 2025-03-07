class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_s = set()
        for i in nums:
            if i in nums_s:
                return i
            nums_s.add(i)