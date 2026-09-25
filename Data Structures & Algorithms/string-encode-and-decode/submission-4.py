class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '(@_@)'
        encode_str = '(-_-)'.join([word  for word in strs])
        return encode_str

    def decode(self, s: str) -> List[str]: 
        if s == '(@_@)':
            return []      
        if s == '':
            return ['']
        decode_lst = s.split('(-_-)')
        return decode_lst
