class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1 #left pointer  we use two pointer method
        r=1 #right pointer
        while r<len(nums): # run the r pointer till the end of an array
            if nums[r]!=nums[r-1]:#check current r not equal to previous r
                nums[l]=nums[r] # change the r to l pointer
                l+=1 #increase l pointer 
                r+=1 #increase r pointer
            else: # if current r is equal to previous r
                r+=1 # increase the r 
        return l
        