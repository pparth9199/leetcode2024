class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l = nums[len(nums)-k::]
        p = nums[:len(nums)-k:]
        nums[:] = l + p
        