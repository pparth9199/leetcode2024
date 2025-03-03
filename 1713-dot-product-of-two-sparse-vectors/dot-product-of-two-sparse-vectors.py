class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {i:val for i, val in enumerate(nums) if val != 0}
 
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        if len(self.d) <= len(vec.d):
            A, B = self.d, vec.d
        else:
            A, B = vec.d, self.d
            
        for i, val in A.items():
            res += val*B.get(i,0)
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)