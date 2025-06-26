class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_array = []

        while x > 0:
            last_digit = x % 10
            x = x // 10
            num_array.append(last_digit)

        arr_len = len(num_array)
        # print(num_array)

        for i in range(0, arr_len // 2):
            if num_array[i] == num_array[arr_len - i - 1]:
                continue
            else:
                return False
        return True