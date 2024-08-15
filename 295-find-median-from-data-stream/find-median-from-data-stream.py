class MedianFinder:

    def __init__(self):
        self.currentMedian = 0
        self.nums=[]

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        l=len(self.nums)
        if l==2:
            self.median =  (self.nums[0]+self.nums[1])/2
        elif l%2==0:
            self.median=((self.nums[l//2-1]+self.nums[(l//2)])/2)
        else:
            self.median=(self.nums[l//2])

        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()