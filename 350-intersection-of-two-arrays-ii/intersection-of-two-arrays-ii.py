class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        minLen = min(len(nums1),len(nums2))
        res=[]
        counter = collections.Counter(nums1 if minLen == len(nums1) else nums2)
        tempCounter = collections.Counter(nums1 if minLen == len(nums1) else nums2)
        iterator = nums2 if minLen == len(nums1) else nums1
        for i in iterator:
            if i in counter and counter[i]>0:
                counter[i]-=1

        for i in tempCounter:
            print(tempCounter)
            if counter[i]!=tempCounter[i]:
                for x in range(tempCounter[i]-counter[i]):
                    res.append(i)
        return res