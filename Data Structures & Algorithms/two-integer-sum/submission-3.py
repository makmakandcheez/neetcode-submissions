class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, v in enumerate(nums):
            val = target - v
            if val in complements:
                return [complements[val], i]
            complements[v] = i

