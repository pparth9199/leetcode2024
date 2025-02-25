class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        non = []
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            else:
                non.append(nums[i])
        i = 0
        for j in range(len(non)):
            nums[i] = non[j]
            i += 1
        for j in range(c):
            nums[i] = 0     
            i += 1   