class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr=[]
        def prefixCalculator(nums):
            nonlocal arr
            n=len(arr)+1
            arr+=nums
            for i in range(1,len(nums)):
                arr[n] += arr[n-1]
                n+=1
        for i in range(len(nums)):
            prefixCalculator(nums[i:])
        arr.sort()
        if len(arr)>500000:print(arr[0],arr[right-1])
        mod =10**9 + 7
        return sum(arr[left-1:right]) % mod