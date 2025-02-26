class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        for i in range(len(possible)):
            if possible[i] == 0:
                possible[i] = -1
        total = sum(possible)
        alice = 0
        for i in range(len(possible)-1):
            alice = alice + possible[i]
            if alice > total - alice:
                return i + 1
        return -1
            