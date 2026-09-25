class Solution:
        def encode(self, strs: list[str]) -> str:
            if not strs:
                return ""
            last_str = strs[0]
            cnt = 0
            str_out = ''
            for i in range(len(strs)):
                if last_str == strs[i]:
                    cnt += 1

                if last_str != strs[i]:
                    str_out += last_str + f'cnt_{cnt}#'                    
                    cnt = 1

                if i == len(strs) - 1:
                    str_out += strs[i] + f'cnt_{cnt}#'

                last_str = strs[i]
            return str_out

        def decode(self, s: str) -> list[str]:
            str_n = re.findall(r'(.*?)cnt_(\d*)#', s)
            lst = []
            # lst = [] if len(str_n) != 0 else [""]
            for i in range(len(str_n)):
                for _ in range(int(str_n[i][1])):
                    lst.append(str_n[i][0])
            return lst
