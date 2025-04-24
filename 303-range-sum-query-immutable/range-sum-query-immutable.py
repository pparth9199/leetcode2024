class NumArray:

    def __init__(self, nums: List[int]):
        self.summed = nums
        for i in range(1,len(nums)):
            self.summed[i] += self.summed[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.summed[right]
        else:
            return self.summed[right]-self.summed[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)