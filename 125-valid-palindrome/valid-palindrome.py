class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = len(s) - 1
        i = 0

        while l >= i:
            if not s[l].isalpha() and not s[l].isdigit():
                l = l -1
                continue

            if not s[i].isalpha() and not s[i].isdigit():
                i = i + 1
                continue
            
            if s[i].lower() == s[l].lower():
                i += 1
                l -= 1
                continue
            else:
                return False
        
        return True

        