class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        t_index = 0
        for c in s:
            if t_index < len(t) and c == t[t_index]:
                t_index += 1
        return len(t) - t_index