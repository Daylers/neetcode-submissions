class Solution:
    def hasDuplicate(self, nums: """List[int]""") -> bool:
        tmp_set = set()
        for num in nums:
            if num in tmp_set:
                return True
            tmp_set.add(num)
        return False
