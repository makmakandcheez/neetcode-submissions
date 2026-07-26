class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{str(len(word))}#{word}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        length = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
                length = int(length)
                i += 1 
                j = i + length
                res.append(s[i:j])
                i = j
                length = ""
            else:
                length += (s[i])
                i += 1
        return res

            



