class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_mp = {}
        right = left = 0

        max_length = 0

        for right in range(len(s)):
            if s[right] in hash_mp:
                left = max(hash_mp[s[right]], left)

            max_length = max(max_length, right - left + 1)
            hash_mp[s[right]] = right + 1
        
        return max_length
        