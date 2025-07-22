from collections import deque
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        current_sum = float("-inf")
        max_sum = float("-inf")
        current_list = deque([])
        for n in nums:
            # print("pre:", current_list, max_sum, n)
            if n not in current_list:
                current_list.append(n)
                current_sum = sum(current_list)
                max_sum = max(max_sum, current_sum)
            else:
                start = 0
                while True:
                    if current_list[start] != n:
                        _ = current_list.popleft()
                    else:
                        break
                _ = current_list.popleft()
                current_list.append(n)
                current_sum = sum(current_list)
                max_sum = max(max_sum, current_sum)
            # print("post:", current_list, max_sum, n)

        return max_sum