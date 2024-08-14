class NumArray:
    nums=[]
    def __init__(self, nums: List[int]):
        self.nums=nums
        for num in range(1,len(nums)):
            self.nums[num] += self.nums[num-1]
        print(self.nums)

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right]-self.nums[left-1] if left>0 else self.nums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)