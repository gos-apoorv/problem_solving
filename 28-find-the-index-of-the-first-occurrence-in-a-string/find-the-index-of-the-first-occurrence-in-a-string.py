class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        str_length = len(haystack)
        sstr_length = len(needle)
        for i in range(0, str_length - sstr_length + 1):
            if haystack[i] == needle[0]:
                t = 0
                while t < sstr_length:
                    if haystack[i+t] != needle[t]:
                        break
                    else:
                        t += 1
                print(i, " ", t, " ")
                if t == sstr_length:
                    return i

        return -1
        