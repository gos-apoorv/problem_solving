class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        def check_palindrome(s: str, lft: int, rht: int) -> bool:

            while lft < rht:
                if s[lft] != s[rht]:
                    return False

                lft += 1
                rht -= 1

            return True

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return check_palindrome(s, left + 1, right) or check_palindrome(s, left, right - 1)

        return True
