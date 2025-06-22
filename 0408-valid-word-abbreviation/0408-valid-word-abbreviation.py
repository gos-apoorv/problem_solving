class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        a_pos = 0
        w_pos = 0
        while w_pos < len(word):
            if a_pos >= len(abbr):
                return False
            elif word[w_pos] == abbr[a_pos]:
                w_pos += 1
                a_pos += 1
                continue
            elif not abbr[a_pos].isdigit() and word[w_pos] != abbr[a_pos]:
                return False
            elif abbr[a_pos].isdigit() and abbr[a_pos].startswith("0"):
                return False
            elif abbr[a_pos].isdigit() and not abbr[a_pos].startswith("0"):
                sub_len = 0
                while a_pos < len(abbr) and abbr[a_pos].isdigit():
                    sub_len = 10 * sub_len + int(abbr[a_pos])
                    a_pos += 1
                w_pos = w_pos + sub_len
        return w_pos == len(word) and a_pos == len(abbr)