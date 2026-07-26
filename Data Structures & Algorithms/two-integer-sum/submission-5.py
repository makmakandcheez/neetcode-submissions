class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = {}
        for i in range(len(nums)):
            if nums[i] in compl:
                return [compl[nums[i]], i]
            c = target - nums[i]
            compl[c] = i
        return [-1, -1]
