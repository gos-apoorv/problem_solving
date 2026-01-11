class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_size = 0
            while i + group_size < len(chars) and chars[i + group_size] == chars[i]:
                group_size += 1
            
            chars[res] = chars[i]
            res += 1
            if group_size > 1:
               str_arr = str(group_size)
               len_str_arr = len(str_arr)
               chars[res: res + len_str_arr] = list(str_arr)
               res += len_str_arr

            i += group_size
        
        return res

        