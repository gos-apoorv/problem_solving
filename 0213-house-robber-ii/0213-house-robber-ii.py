class Solution:
    def rob(self, nums: List[int]) -> int:
        num_len = len(nums)

        if num_len < 1:
            return 0
        elif num_len == 1:
            return nums[0]
        
        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))
    
    def rob_simple(self, nums: List[int]) -> int:
        t1 =0
        t2 =0

        for c in nums:
            temp = t1
            t1 = max(c + t2, t1)
            t2 = temp

        
        return t1

        