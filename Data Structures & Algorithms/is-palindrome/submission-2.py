class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        low_s = s.lower()
        low_s = low_s.replace(" ","")

        i = 0
        j = len(low_s) - 1

        while i < j:
            while i < j and not low_s[i].isalnum():
                i += 1
            while i < j and not low_s[j].isalnum():
                j -= 1
            if low_s[i] != low_s[j]:
                return False
            i += 1
            j -= 1
        return True