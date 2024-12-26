class Solution:
    def partitionString(self, s: str) -> int:

        last_seen = [-1] * 26
        count = 0
        # substring helps to count occurence of same characters in different substring
        substring = 0

        for i in range(len(s)):
            if last_seen[ord(s[i]) - ord('a')] >= substring:
                count += 1
                substring = i
            last_seen[ord(s[i]) - ord('a')] = i
        return count+1