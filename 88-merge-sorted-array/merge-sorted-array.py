class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        j = 0
        for i in range(m+n):
            if nums1[i] == 0 and j < n:
                nums1[i] = nums2[j]
                j = j + 1
        nums1.sort()
                                                  
        