class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1 
            end = n - 1

            while start < end:
                sum_n =  nums[i] + nums[start] + nums[end]
                if sum_n == 0:
                    result.append([nums[i],nums[start],nums[end]])
                    while start < n - 1 and nums[start] == nums[start + 1]:
                        start += 1
                    start += 1
                    continue
                elif sum_n < 0:
                    start += 1
                else:
                    end -= 1
        return result