class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # for i in range(0, len(nums)-1):
        #     k = i+1
        #     for j in range(i+1, len(nums)):
        #         s = [nums[i]]
        #         t = nums[i] + nums[j]
        #         if 0 - t in nums[k+1:]:
        #             s.append(nums[j])
        #             s.append(0-t)
        #         s.sort()
        #         if s not in ans and len(s) == 3:
        #             ans.append(s)
        #         k = k + 1
        # return ans
        nums.sort()
        ans = []
        s = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    s.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l += 1
        for i in s:
            ans.append(list(i))
        return ans


