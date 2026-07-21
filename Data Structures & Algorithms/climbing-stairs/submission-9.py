class Solution:
    def climbStairs(self, n: int) -> int:
        minus_one, minus_two = 1, 1
        res = minus_one

        for i in range(2, n+1):
            res = minus_one + minus_two
            minus_two = minus_one
            minus_one = res
        
        return res






        