class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for i in counter:
            if counter[i] > len(nums)//2:
                return i