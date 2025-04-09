class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l,r=0,len(nums)-1
        expected_len = nums[-1] - nums[0] + 1 
        no_of_missing = expected_len - len(nums) 
        if k > no_of_missing: 
            return nums[-1] + k - no_of_missing
            
        while l+1<r:
            mid = (l+r)//2
            missing = nums[mid] - nums[l] - mid +l
            if missing < k:
                l=mid
                k-=missing
            else:
                r=mid

        return nums[l] + k