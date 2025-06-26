class Solution:
    def romanToInt(self, s: str) -> int:

        num_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num_array = list(s)

        print(num_dict)
        print(num_array)
        total_sum = prev_num = curr_num = 0
        for i in num_array:
            curr_num = num_dict[i]
            if curr_num > prev_num:
                total_sum = total_sum + curr_num - (2 * prev_num)
            else:
                total_sum = total_sum + curr_num
            prev_num = curr_num

        return total_sum
