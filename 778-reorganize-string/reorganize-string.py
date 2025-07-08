from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:

        char_count = Counter(s)
        print(char_count)

        str_len = len(s)
        max_char_len = 0
        max_char = ""
        for char, count in char_count.items(): 
            if count > max_char_len:
                max_char_len = count
                max_char = char
            
            if max_char_len > (str_len + 1 )//2:
                return ""

        ans = [''] * str_len
        index = 0
        while char_count[max_char] > 0:
            # print("index=",index,"  ans=",ans, " char_count[max_char]=", char_count[max_char])
            ans[index] = max_char
            char_count[max_char] -= 1
            index += 2

        for char, count in char_count.items():
            while count > 0:
                if index >= str_len:
                    index = 1

                ans[index] = char
                count -= 1
                index += 2

        return "".join(ans)