class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in arr:
            heapq.heappush(heap,(abs(i-x),i))
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        res.sort()
        return res