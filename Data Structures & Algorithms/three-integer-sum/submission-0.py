class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # [-1,0,1,2,-1,-4]
        
        for i in range(len(nums)):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target and [nums[i], nums[l], nums[r]] not in res:
                    res.append([nums[i], nums[l], nums[r]])
                elif sum > target:
                    r -= 1
                else:
                    l += 1 
        return res