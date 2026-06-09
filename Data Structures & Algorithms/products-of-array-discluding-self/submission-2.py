class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_idx = None
        for i, num in enumerate(nums):
            if num == 0:
                if zero_idx is not None:
                    print("More than one 0 found.")
                    product = 0
                    break
                else:
                    zero_idx = i
            else:
                product *= num

        print("Product = " + str(product))
        ans = [0] * len(nums)
        if product == 0:
            return ans
        elif zero_idx:
            ans[zero_idx] = product
            return ans
        else:
            for i in range(len(nums)):
                ans[i] = product // nums[i]
            return ans
                