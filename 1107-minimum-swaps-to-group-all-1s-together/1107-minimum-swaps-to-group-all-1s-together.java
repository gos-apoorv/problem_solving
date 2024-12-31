class Solution {
    public int minSwaps(int[] data) {

        int ones = Arrays.stream(data).sum();
        int cnt_one = 0, max_one =0;

        int left= 0, right = 0;
        // loop through each element of array starting from 0
        while (right < data.length)
        {
            // Keep on adding current value to total 1 encountered so far
            cnt_one += data[right++];

            // To window slide in sub-array with size of max 1s in array
            if(right - left > ones){
                cnt_one -= data[left++]; 
            }

            max_one = Math.max(max_one, cnt_one);
        }
        return ones - max_one; 
        
    }
}