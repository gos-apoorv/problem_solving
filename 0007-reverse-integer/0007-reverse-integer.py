class Solution:
    def reverse(self, x: int) -> int:
        new_num = 0
        num_sign = -1 if x < 0 else 1
        abs_num = abs(x)
        while abs_num > 0:
            last_dig = abs_num % 10
            new_num = (10 * new_num) + last_dig

            if new_num > 2**31 -1:
                return 0
            abs_num = abs_num // 10
        return num_sign * new_num