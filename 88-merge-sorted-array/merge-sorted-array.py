class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0

        while i < m + n and j < n:
            if nums1[i] == 0 and i >= m:
                nums1[i] = nums2[j]
                j += 1
                i += 1
            elif nums2[j] < nums1[i]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
                m += 1
            else:
                i += 1
        