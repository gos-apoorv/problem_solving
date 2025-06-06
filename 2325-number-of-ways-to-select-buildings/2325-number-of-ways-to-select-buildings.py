class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = 0
        one = 0
        zero = 0
        one_zero = 0
        zero_one = 0

        for c in s:
            if c == '0':
                zero += 1
                one_zero += one
                ways += zero_one
            else:
                one += 1
                zero_one += zero
                ways += one_zero
                # print("one", '--', c, '--', zero, '--', one, '--', one_zero, '--', zero_one, '--', ways)
        return ways