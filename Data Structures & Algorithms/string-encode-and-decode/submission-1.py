class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = ""
        words = "#"
        for word in strs:
            lengths += str(len(word)) + "%"
            words += word
        msg = lengths + words
        print(msg)
        return msg

    def decode(self, s: str) -> List[str]:
        print(s)
        counts = []
        s_idx, num = 0, 0
        for i, c in enumerate(s):
            if c == "#":
                s_idx = i+1
                break
            if c == "%":
                counts.append(int(num))
                num=0
            else:
                num = num * 10 + int(c)

        result = []
        for count in counts:
            word = s[s_idx:s_idx+count]
            s_idx += count
            result.append(word)
        
        return result
