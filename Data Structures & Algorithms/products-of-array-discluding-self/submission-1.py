class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [0] * len(nums)
        right_products = left_products.copy()

        for i, num in enumerate(nums):
            if i == 0:
                left_products[i] = 1
            else:
                left_products[i] = left_products[i-1] * nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                right_products[i] = 1
            else:
                right_products[i] = right_products[i+1] * nums[i+1]

        lst_out = [a * b for a, b in zip(left_products, right_products)]

        return lst_out