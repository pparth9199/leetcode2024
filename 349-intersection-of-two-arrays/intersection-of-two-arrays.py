class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        minLen = min(len(nums1),len(nums2))
        res=[]
        counter = collections.Counter(nums1 if minLen == len(nums1) else nums2)
        tempCounter = collections.Counter(nums1 if minLen == len(nums1) else nums2)
        iterator = nums2 if minLen == len(nums1) else nums1
        for i in iterator:
            if i in counter:
                counter[i]-=1

        for i in tempCounter:
            print(tempCounter[i],i)
            if counter[i]!=tempCounter[i]:
                res.append(i)
        return res