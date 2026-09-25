class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_out = dict()
        for i in range(len(strs)):
            str_key = tuple(sorted(strs[i]))
            if dict_out.get(str_key, False):
                dict_out[str_key].append(strs[i])
            else:
                dict_out[str_key] = [strs[i]]
            # print(dict_out[str_key])
        return [lst for lst in dict_out.values()]
            # print(dict_out)


        