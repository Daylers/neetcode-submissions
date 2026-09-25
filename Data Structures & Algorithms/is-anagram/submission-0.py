class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s_dict.get(s[i]) == None:
                    s_dict[s[i]] = 0
                if t_dict.get(t[i]) == None:
                    t_dict[t[i]] = 0
                s_dict[s[i]] += 1
                t_dict[t[i]] += 1
            if s_dict == t_dict:
                return True
        return False