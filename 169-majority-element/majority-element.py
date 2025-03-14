class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        cache = Counter(nums)

        for k,v in cache.items():
            if v>n:
                return k

            