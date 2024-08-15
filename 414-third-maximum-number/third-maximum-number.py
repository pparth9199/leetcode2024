class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numSet =set(nums)
        stack=[]
        if len(numSet)<3:
            return max(numSet)
        for i in numSet:
            heapq.heappush(stack,-i)
        k=1
        print(stack)
        while k<3:
            heapq.heappop(stack)
            k+=1
        
        return -stack[0]