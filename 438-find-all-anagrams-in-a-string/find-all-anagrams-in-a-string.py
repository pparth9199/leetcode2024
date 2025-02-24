class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # res = []
        # if len(s) < len(p):
        #     return res
        # l = 0
        # r = len(p)
        # anagram = True
        # while r < len(s)+1:
        #     ana = s[l:r]
        #     word = list(p)
        #     print(ana)
        #     for i in ana:
        #         if i not in word:
        #             anagram = False
        #             break
        #         word.remove(i)
        #     if anagram and not word:
        #         res.append(l)
        #     l = l + 1
        #     r = r + 1
        #     anagram = True
        # return res
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        # build hashmap
        for ch in p: hm[ch] += 1

        # initial full pass over the window
        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1
            
        # slide the window with stride 1
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm: 
                hm[s[i+pL]] -= 1
                
            # check whether we encountered an anagram
            if all(v == 0 for v in hm.values()): 
                res.append(i+1)
                
        return res
            