class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        pos = len(s)-1

        while pos >= 0 and s[pos] == " ":
            pos = pos -1

        length = 0
        while pos >= 0 and s[pos] != " ":
            pos = pos -1
            length += 1
        
        return length
        