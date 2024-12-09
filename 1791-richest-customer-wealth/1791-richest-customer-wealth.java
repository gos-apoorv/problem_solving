class Solution {
    public int maximumWealth(int[][] accounts) {
        int max_amount = 0;
        // Iterate through each array
        for(int i=0; i < accounts.length; i++)
        {
            int total = 0;
            for(int j=0; j < accounts[0].length; j++)
            {
                // Find total of each customer
                total +=  accounts[i][j];
            }
            // Find max of previous sum and current total
            max_amount = Math.max(max_amount, total);
        }
        return max_amount;
    }
}