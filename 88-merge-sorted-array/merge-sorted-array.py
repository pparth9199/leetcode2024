class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n - 1
        i = m - 1
        j = n - 1
        while j >= 0:
            if i < 0 or nums1[i] <= nums2[j]:
                nums1[l] = nums2[j]
                j = j - 1
            elif nums1[i] > nums2[j]:
                nums1[l] = nums1[i]
                i = i - 1
            l = l - 1
        