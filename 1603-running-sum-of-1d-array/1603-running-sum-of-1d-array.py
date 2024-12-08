class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # Time Complexity: O(n)
        # Space Coplexity: O(n)
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
            
        return nums
        