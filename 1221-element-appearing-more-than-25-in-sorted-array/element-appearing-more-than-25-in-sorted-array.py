# class Solution:
#     def findSpecialInteger(self, arr: List[int]) -> int:
#         if not arr: return 0
#         if len(set(arr)) == 1:
#             return arr[0]


#         cache = defaultdict(int)
#         quarter = len(arr)/4
#         for i in arr:
#             cache[i] += 1
#             if cache[i] > quarter:
#                 return i
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in range(len(arr) - len(arr)//4):
            if arr[i] == arr[i + len(arr)//4]:
                return arr[i]