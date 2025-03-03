class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        distance = []
        for x, y in points:
            dist = x**2 + y**2
            distance.append((dist, (x, y))) #we append to the distance array here instead of heappush() as append() takes O(1) time while heappush() takes O(log n) time
        heapq.heapify(distance) #O(n)
        for i in range(k):
            ans.append(heappop(distance)[1]) #O(logn)
        return ans