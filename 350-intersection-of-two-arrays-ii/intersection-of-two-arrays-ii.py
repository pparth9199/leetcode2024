class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct = Counter(nums1)
        result = []
            
        for n2 in nums2:
            if n2 in dct and dct[n2]>0:
                result.append(n2)
                dct[n2] -= 1
                
        return result