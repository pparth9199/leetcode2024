class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l,r=0,len(nums)-1
        diff = nums[-1] - nums[0] + 1 # complete length
        missing = diff - len(nums) # complete length - real length
        if k > missing: # if k is larger than the number of mssing words in sequence
            return nums[-1] + k - missing
        while l+1<r:
            mid = (l+r)//2
            missing = nums[mid] - nums[l] - mid +l
            if missing < k:
                l=mid
                k-=missing
            else:
                r=mid

        return nums[l] + k