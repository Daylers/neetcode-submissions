class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_nums = dict()
        for i in range(len(nums)):
            if cnt_nums.get(nums[i], False):
                cnt_nums[nums[i]] += 1            
            else:
                cnt_nums[nums[i]] = 1
        lst_out = [key for key, value in sorted(cnt_nums.items(), key=lambda x:x[1], reverse=True)]
        return lst_out[:k]