class Solution:
    def jump(self, nums: List[int]) -> int:

        num_len = len(nums)

        if num_len < 2:
            return 0
        count = 0
        last = next = 0

        while next < num_len-1:
            temp = next
            next = max(nums[j] + j for j in range(last, next + 1))
            last = temp
            count += 1

        
        return count

        