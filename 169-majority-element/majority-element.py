class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = Counter(nums)
        for i in hash_map:
            if hash_map[i]>(len(nums)//2):
                return i
        