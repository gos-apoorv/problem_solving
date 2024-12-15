class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor_list = []

        # Calculate factor by iterating through all numbers from 1 to n
        for num in range(1, n + 1):
            # if current number num is a factor of n, add to list
            if (n % num) == 0:
                factor_list.append(num)

                # If current number is kth , then return
                if len(factor_list) == k:
                    return num

        return -1