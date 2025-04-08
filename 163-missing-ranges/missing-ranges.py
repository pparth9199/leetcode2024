class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        p1,p2=0,1
        if not nums:
            return [[lower,upper]]
        res = []
        if nums[p1]>lower:
            res.append([lower,nums[p1]-1])
        while p2<len(nums):
            if nums[p2]-nums[p1]>1:
                res.append([nums[p1]+1, nums[p2]-1])
            p1+=1
            p2+=1
        if nums[-1]<upper:
            res.append([nums[-1]+1,upper])

        return res