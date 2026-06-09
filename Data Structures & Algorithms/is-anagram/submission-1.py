class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for c in s:
            if count.get(c):
                count[c]+=1
            else:
                count[c]=1
        for c in t:
            if count.get(c):
                count[c]-=1
            else:
                return False
        for val in count.values():
            if val!=0:
                return False
        return True