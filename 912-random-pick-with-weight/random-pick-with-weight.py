class Solution:

    def __init__(self, w: List[int]):
        self.range = -1
        self.ranges = []
        for weight in w:
            self.range+=weight
            self.ranges.append(self.range)
    def search(self, target):
        left = 0
        right = len(self.ranges)-1
        while left<right:
            mid = (left+right)//2
            if self.ranges[mid]<target:
                left = mid+1
            else:
                right = mid
        return left
        


    def pickIndex(self) -> int:
        target = random.randint(0,self.range)
        return self.search(target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()