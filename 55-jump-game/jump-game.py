class Solution:
    def __init__(self):
        self.nums = []
        self.memo = []

# This is using Top down approach
    # def canJumpFromPosition(self, position):
    #     if self.memo[position] != -1:
    #         return self.memo[position] == 1

    #     furthest_jump = min(
    #        position +  self.nums[position],
    #        len(self.nums) - 1
    #     )

    #     for pos in range(position + 1, furthest_jump + 1):
    #         if self.canJumpFromPosition(pos):
    #             self.memo[pos]  = 1
    #             return True
    #     self.memo[position]  = 0
    #     return False

    # def canJump(self, nums: List[int]) -> bool:
    #     self.nums = nums
    #     self.memo = [-1] * len(nums)

    #     self.memo[-1] = 1
    #     return self.canJumpFromPosition(0)

# This is using greedy aproach
    def canJump(self, nums: List[int]) -> bool:
        num_len = len(nums)
        last_pos = num_len - 1

        for i in range(last_pos, -1, -1):

            if nums[i] + i >= last_pos:
                last_pos = i
            
        return last_pos == 0

