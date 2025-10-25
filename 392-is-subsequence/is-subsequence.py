class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_len = len(t)
        s_len = len(s)
        i = 0
        j = 0

        if s == "":
            return True

        while j <= t_len-1 and i <= s_len-1:
            print("s==", s[i], "||t==", t[j])
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i == s_len:
            return True
        return False
        