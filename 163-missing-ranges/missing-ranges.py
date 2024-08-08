class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums)==0:
            return[[lower,upper]]
        res=[]
        intermediate=[]
        for i in range(len(nums)):
            if i==0 and nums[i]>lower:
                intermediate=[lower,nums[i]-1]
                res.append(intermediate)
            elif nums[i-1]!=nums[i]-1 and i!=0:
                intermediate=[nums[i-1]+1,nums[i]-1]
                res.append(intermediate)
        if nums[-1]<upper:
            intermediate=[nums[-1]+1,upper]
            res.append(intermediate)
                
        return res