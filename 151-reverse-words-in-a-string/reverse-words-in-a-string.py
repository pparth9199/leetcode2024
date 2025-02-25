class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        sl = s.split(" ")
        l = 0
        r = len(sl) - 1
        while l < r:
            sl[l], sl[r] = sl[r], sl[l]
            l = l + 1
            r = r - 1
        new = ""
        for i in sl:
            if i == "":
                continue
            new = new + i + " "
        return new.strip()