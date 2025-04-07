class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - k
        while low < high:
            mid = low + (high - low) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                high = mid
            else:
                low = mid + 1
        return arr[low: low + k]