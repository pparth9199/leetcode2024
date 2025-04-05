class SparseVector:
    def __init__(self, nums: List[int]):
        self.v1=nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in range(len(self.v1)):
            res += self.v1[i]*vec.getAtIndex(i)
        return res
    
    def getAtIndex(self,index):
        return self.v1[index]

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)