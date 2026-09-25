class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        list_seq = []
        cnt = 0
        for i in range(len(nums)):
            if i == 0:
                cnt += 1
                continue

            if nums[i] - nums[i-1] == 1:
                cnt += 1
            elif nums[i] - nums[i-1] == 0:
                continue
            else:
                list_seq.append(cnt)
                cnt = 1
        list_seq.append(cnt)

        return max(list_seq)