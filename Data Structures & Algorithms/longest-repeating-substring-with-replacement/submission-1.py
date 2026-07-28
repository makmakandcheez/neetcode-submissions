class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        counts = {}
        l = r = 0
        res = 0
        window_size = 0
        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxf = max(maxf, counts[s[r]])
            window_size += 1
            while (window_size - maxf > k):
                counts[s[l]] -= 1
                window_size -= 1
                l +=1
            res = max(res, window_size)
            r += 1
        
        return res

