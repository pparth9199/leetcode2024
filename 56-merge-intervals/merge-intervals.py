class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        idx = 0
        n = len(intervals)

        for i in range(1, n):
            previous_interval = output[idx]
            curr_interval = intervals[i]
            if curr_interval[0] <= previous_interval[1]:
                output[idx] = [min(previous_interval[0],curr_interval[0]), max(previous_interval[1],curr_interval[1])]
            else:
                output.append(curr_interval)
                idx+=1

        return output 




