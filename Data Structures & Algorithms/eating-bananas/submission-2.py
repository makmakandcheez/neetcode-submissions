class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = max(piles)

        return self.search(1, max(piles), piles, h, max(piles))
    
    def search(self, l: int, r: int, piles: List[int], h: int, min_speed: int) -> int:
        if l > r:
            return min_speed
        
        m = l + (r - l) // 2
        time = 0
        for p in piles:
            time += -(p // -m)
        if time > h:
            return self.search(m + 1, r, piles, h, min_speed)
        else:
            return self.search(l, m - 1, piles, h, min(min_speed, m))
            


