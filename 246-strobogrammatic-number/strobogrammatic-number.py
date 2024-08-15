class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        l, r = 0, len(num) - 1
        mapping = {
            "0": "0",
            "1": "1",
            "8": "8",
            "6": "9",
            "9": "6",
        }

        while l <= r:
            if num[l] in mapping and mapping[num[l]] == num[r]:
                l += 1
                r -= 1
            else:
                return False
        return True