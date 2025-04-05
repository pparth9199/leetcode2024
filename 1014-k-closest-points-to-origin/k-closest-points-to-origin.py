class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculateDistance(x1,y1):
            return x1**2+y1**2
        heap = []
        for i in points:
            heapq.heappush(heap,(-calculateDistance(i[0],i[1]),i))
            if len(heap)>k:
                heapq.heappop(heap)
    
        return [x[1] for x in heap]
