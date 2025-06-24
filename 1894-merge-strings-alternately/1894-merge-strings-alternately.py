class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_pos = 0
        w2_pos = 0
        final_str = ''
        while w1_pos < len(word1) or w2_pos < len(word2):
            final_str = (final_str + word1[w1_pos]) if w1_pos < len(word1) else final_str
            final_str = (final_str + word2[w2_pos]) if w2_pos < len(word2) else final_str

            w1_pos += 1
            w2_pos += 1
        return final_str