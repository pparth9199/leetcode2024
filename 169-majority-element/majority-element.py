class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        currentMax = 0
        majorityElement = -1
        for i in counter:
            if counter[i] > currentMax:
                currentMax = counter[i]
                majorityElement = i

        return majorityElement