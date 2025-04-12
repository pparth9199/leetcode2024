class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0
        
        left = 0
        freq = defaultdict(int)
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len