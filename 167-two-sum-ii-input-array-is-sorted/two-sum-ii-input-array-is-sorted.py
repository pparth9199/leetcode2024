class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers)-1

        while low < high:
            sum: int = numbers[low] + numbers[high]
            if sum < target:
                low += 1
            elif sum > target:
                high -= 1
            else:
                return [low+1, high+1]
        
        return None