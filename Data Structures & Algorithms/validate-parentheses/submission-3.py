class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        br_mp = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in br_mp and stack:
                head = stack.pop()
                if br_mp[c] != head:
                    return False
            else:
                stack.append(c)
            
        return not stack
        