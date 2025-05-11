class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def twoSum(l,r,target):
            while l < r:
                summ = nums[l] + nums[r]
                if summ == target:
                    res.append([-target, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif summ < target:
                    l += 1
                else:
                    r -= 1


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l,r=i+1,len(nums)-1

            twoSum(l,r,target)

        return res

            
