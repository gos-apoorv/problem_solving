class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        key_dict = {}
        i = 0

        for c in key:
            if c == ' ':
                continue
            dict_char =key_dict.get(c, None)

            if not dict_char:
                key_dict[c] = chr(ord('a') + i)
                # print(c,"-->",i, "-->", ord('a') + i, "-->",chr(ord('a') + i), "-->", len(list(key_dict.keys())))
                i += 1

            if len(list(key_dict.keys())) >= 26:
                break

        result = ""
        for m in message:
            dict_char = key_dict.get(m, m)
            result += dict_char
        
        return result