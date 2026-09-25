class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_cnt = {}
        for num in nums:
            if dict_cnt.get(num) == None:
                dict_cnt[num] = 1
            else:
                dict_cnt[num] += 1
        # print(dict_cnt.values())
        sorted_data = sorted(dict_cnt.items(), key=lambda item: item[1], reverse=False)
        # print(sorted_data)

        out = sorted_data[-k:]
        return [num[0] for num in out]
        # print([i[0] for i in out])
        