class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = collections.Counter(p)
        s_dict = collections.Counter(s[:len(p)-1]) 
        l = 0
        # final result list
        res = []
        # We iterate over the string s, and in each step we check if s_dict and p_dict match
        for r in range(len(p)-1, len(s)):
            # updating the counter & adding the character
            s_dict[s[r]] += 1
            # checking if counters match
            if s_dict == p_dict:
                res.append(l)
            # remove the first element from counter
            s_dict[s[l]] -= 1
            l += 1
            
        return res