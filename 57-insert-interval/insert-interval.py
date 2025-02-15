class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = []
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][0]:
            new.append(intervals[i])
            i = i + 1
        
        if not new or new[-1][1] < newInterval[0]:
            new.append(newInterval)
        else:
            new[-1][1] = max(new[-1][1], newInterval[1])

        while i < len(intervals):
            tmp = intervals[i]
            if new[-1][1] < tmp[0]:
                new.append(tmp)
            else:
                new[-1][1] = max(new[-1][1], tmp[1])
            i = i + 1
        return new

