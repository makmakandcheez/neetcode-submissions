class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = sys.maxsize
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] > nums[r]:
                m = l + (r - l) // 2
                smallest = min(nums[m], smallest)
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                return min(nums[l], smallest)


        return smallest