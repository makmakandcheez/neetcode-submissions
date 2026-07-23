class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], nums[1]
        highest = dp[0]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + highest)
            highest = max(highest, dp[i-1])
        
        return max(dp[-1], dp[-2])