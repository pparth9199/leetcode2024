class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])

        res = []

        for interval in intervals:
            start,end = interval

            if not res or res[-1][1]<start:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1],end)
        return res