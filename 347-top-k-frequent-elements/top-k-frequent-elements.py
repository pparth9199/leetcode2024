class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        countDict = Counter(nums)
    
        heap = []
        for num, count in countDict.items():
            heapq.heappush(heap, [-count, num])
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans