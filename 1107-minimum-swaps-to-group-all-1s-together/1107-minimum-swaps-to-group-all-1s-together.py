class Solution:
    def minSwaps(self, data: List[int]) -> int:

        # Calculate number of one in list
        count = sum(data)
        count_one = swaps = 0

        if count == 1:
            return swaps

        left = right = 0

        # Check for sub array to bring all 1s togther
        while right < len(data):
            # Increase the sum of ones
            count_one += data[right]
            # increment the pointer
            right += 1

            if right - left > count:
                count_one -= data[left]
                left += 1

            swaps = max(swaps, count_one)


        return count - swaps