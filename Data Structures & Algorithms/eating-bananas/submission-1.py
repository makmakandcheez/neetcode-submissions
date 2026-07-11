class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed = r

        while l <= r:
            m = l + (r - l) // 2
            time = 0
            for p in piles:
                time += math.ceil(float(p) / m)
            if time > h:
                l = m + 1
            else:
                r = m - 1
                min_speed = min(m, min_speed)
        
        return min_speed
            


