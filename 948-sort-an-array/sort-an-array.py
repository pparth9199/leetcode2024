class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []

        for i in nums:
            heapq.heappush(heap,i)
        for i in range(len(nums)):
            curr = heapq.heappop(heap)
            nums[i]=curr
        heap=[]
        return nums