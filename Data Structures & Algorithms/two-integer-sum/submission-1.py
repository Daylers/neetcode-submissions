class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = {i: num for i, num in enumerate(nums)}

        for i, x in nums_dict.items():
            for j, y in nums_dict.items():
                if x + y == target and i != j:
                    return [i, j]