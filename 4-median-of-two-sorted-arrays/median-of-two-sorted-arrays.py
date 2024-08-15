class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def calculateMedian(combinedNums):
            combinedNumsLength = len(combinedNums)
            medianIndex = combinedNumsLength//2
            if combinedNumsLength%2==0:
                return (combinedNums[medianIndex]+combinedNums[medianIndex-1])/2
            else:
                return combinedNums[medianIndex]
              
        if not nums1 or not nums2 or nums1[-1]<nums2[0]:
            return calculateMedian(nums1+nums2)

        return calculateMedian(sorted(nums1+nums2))
        
                
            