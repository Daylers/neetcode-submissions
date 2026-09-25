class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_out = {}
        for word in strs:            
            key_word = ''.join(sorted(word))
            if key_word not in dict_out.keys():
                dict_out[key_word] = [word]
            else:
                dict_out[key_word].append(word)
        return list(dict_out.values())