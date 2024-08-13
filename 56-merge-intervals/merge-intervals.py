class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        l,r=0,1
        res=[]
        endFlag=False
        intervals.sort()
        while r<len(intervals):
            
            if intervals[l][1]>=intervals[r][0]:
                intervals[r]=[intervals[l][0],max(intervals[r][1],intervals[l][1])]
                intervals[l]=None
                if r==len(intervals)-1:
                    endFlag=True
            r+=1
            l+=1
        if not endFlag:intervals[-1] = intervals[l]
        res = list(filter(lambda x:x!=None,intervals))
        return res