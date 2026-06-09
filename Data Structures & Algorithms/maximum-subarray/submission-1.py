class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=-9999999
        sum=0
        for num in nums:
            if num > num + sum:
                sum = num
            else:
                sum += num
                
            if sum > best:
                best = sum
                
        return best