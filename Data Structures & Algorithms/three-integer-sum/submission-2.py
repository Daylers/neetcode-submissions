class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst_answer = []
        nums.sort()
        # print(nums)
        for i in range(len(nums)):
            a = 0
            b = len(nums) - 1            
            for j in range(len(nums)):
                if a == i:
                    a += 1
                    continue
                if b == i:
                    b -= 1
                    continue
                if a == b:
                    break

                # print('i', nums[i], 'a', nums[a], 'b', nums[b], 'sum', nums[i] + nums[a] + nums[b])

                if nums[i] + nums[a] + nums[b] < 0:
                    a += 1
                elif nums[i] + nums[a] + nums[b] > 0:
                    b -= 1
                else:
                    triple = sorted([nums[i], nums[a], nums[b]])
                    if triple not in lst_answer:
                        lst_answer.append(triple)
                    b -= 1
        return lst_answer