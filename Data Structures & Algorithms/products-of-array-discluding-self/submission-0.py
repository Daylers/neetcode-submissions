class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        lst_out = []
        for num in nums:
            numb = 1 if num == 0 else num
            prod = prod * numb
        for i, num in enumerate(nums):
            if 0 in (nums[:i] + nums[i+1:]):
                lst_out.append(0)
            else:
                lst_out.append(prod // (num if num !=0 else 1))

        return lst_out