class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            sum = 0
            while (n > 0):
                sum += int((n % 10)**2)
                n //= 10
            print(sum)
            if sum == 1:
                return True
            elif sum in seen:
                return False
            else:
                seen.add(sum)
            n = sum
        