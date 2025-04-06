class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        l = len(nums)
        for i in nums:
            count[i] +=1
            if count[i] > l//2:
                return i
    
