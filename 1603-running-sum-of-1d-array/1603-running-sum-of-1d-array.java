class Solution {
    public int[] runningSum(int[] nums) {

        // Time Complexity: O(n)
        //  Space Coplexity: O(n)
        for (int i = 1; i <= nums.length - 1; i++) {
            nums[i] = nums[i - 1] + nums[i];
        }

        return nums;
    }
}