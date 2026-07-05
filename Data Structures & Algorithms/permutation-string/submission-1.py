class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = [0] * 26
        for c in s1:
            s1_counts[ord(c) - ord('a')] += 1
        
        l, r = 0, 0
        window_counts = [0] * 26

        
        # Check counts
        while r < len(s2):
            if r - l + 1 > len(s1):
                window_counts[ord(s2[l]) - ord('a')] -= 1
                l += 1
            window_counts[ord(s2[r]) - ord('a')] += 1
            r += 1
            if window_counts == s1_counts:
                return True
        
        return False