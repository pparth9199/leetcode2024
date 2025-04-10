class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key= lambda x:x[0])
        res=[]
        for interval in intervals:
            start,end = interval

            if not res or res[-1][1]<start:
                res.append([start,end])
            else:
                res[-1][1] = max(res[-1][1],end)

        return res
