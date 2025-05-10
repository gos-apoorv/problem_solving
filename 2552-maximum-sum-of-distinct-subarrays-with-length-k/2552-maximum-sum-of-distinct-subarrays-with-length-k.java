class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int  begin = 0, end =0;
        long ans = 0, currentSum = 0;
        
        HashMap<Integer, Integer> numSet = new HashMap<Integer, Integer>();

        while(end< nums.length){
            int currentNum = nums[end];
            int lastOccurence = numSet.getOrDefault(currentNum, -1);

            while(begin <= lastOccurence || end - begin + 1> k){
                currentSum -= nums[begin];
                begin += 1;  
            }

            currentSum += nums[end];
            numSet.put(currentNum, end);
            if(end - begin + 1 == k){
                ans = Math.max(ans, currentSum);
            }
            end += 1;
        }

        return ans;
    }
}