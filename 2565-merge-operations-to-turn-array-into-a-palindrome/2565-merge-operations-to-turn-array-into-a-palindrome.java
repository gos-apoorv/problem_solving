class Solution {
    public int minimumOperations(int[] nums) {

        int left = 0, right =  nums.length-1, prev =  0, counter = 0;

        while(left <= right){
            if(nums[left]==nums[right]){
                left++;
                right--;
            } else if(nums[left] < nums[right]){
                prev = nums[left];
                nums[++left] = nums[left] + prev;
                counter++;
            } else if(nums[left] > nums[right]){
                prev = nums[right];
                nums[--right] = nums[right] + prev;
                counter ++;
            }        
        }

        return counter;

    }
}