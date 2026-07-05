class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        mp = {} # key=char, val=index last seen

        for r in range(len(s)):
            if s[r] in mp and mp[s[r]] in range(l, r):
                l = mp[s[r]] + 1
            mp[s[r]] = r
            print(mp)
            print(l, r)
            longest = max(r - l + 1, longest)
        
        return longest
