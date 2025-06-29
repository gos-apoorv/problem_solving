class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        char_array = []
        str_len = len(s)
        char_jump = 2*numRows -2

        for curr_row in range(numRows):
            pos = curr_row

            while pos < str_len:
                char_array.append(s[pos])

                if curr_row != 0 and curr_row != numRows-1:
                    second_char = pos + char_jump - 2*curr_row

                    if second_char < str_len:
                        char_array.append(s[second_char])

                pos += char_jump

        return "".join(char_array)