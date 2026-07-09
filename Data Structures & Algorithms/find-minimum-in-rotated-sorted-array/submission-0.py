class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = sys.maxsize
        for n in nums:
            smallest = min(n, smallest)
        return smallest