class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = nums[0]

        # Calculate prefix
        for i in range(1, len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            # res[i] = res[i-1] * nums[i-1]

        # Calculate suffix
        suffix = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res