class Solution:
    def __init__(self):
        self.nums = []
        self.memo = []

    def canJumpFromPosition(self, position):
        if self.memo[position] != -1:
            return self.memo[position] == 1

        furthest_jump = min(
           position +  self.nums[position],
           len(self.nums) - 1
        )

        for pos in range(position + 1, furthest_jump + 1):
            if self.canJumpFromPosition(pos):
                self.memo[pos]  = 1
                return True
        self.memo[position]  = 0
        return False

    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        self.memo = [-1] * len(nums)

        self.memo[-1] = 1
        return self.canJumpFromPosition(0)