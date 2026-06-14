class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        l = 0
        longest = 0
        window_map = {}

        for r in range(len(s)):
            if s[r] in window_map:
                l = max(l, window_map[s[r]] + 1)
            window_map[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest
