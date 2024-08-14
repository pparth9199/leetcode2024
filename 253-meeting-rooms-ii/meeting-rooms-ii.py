class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms=[intervals[0]]
        
        for i in range(1,len(intervals)):
            replaced = False
            for x in range(len(rooms)):
                if rooms[x][1]<=intervals[i][0]:
                    rooms[x]=intervals[i]
                    replaced=True
                    break
            if not replaced:
                rooms.append(intervals[i])
                    
        return len(rooms)
                    