class Solution {
    public long numberOfWays(String s) {
        long ways = 0;
        int zero = 0;
        int ones = 0;
        long zeroOne = 0;
        long oneZero = 0;
        for(int i =0; i < s.length(); i++)
        {
            if(s.charAt(i)=='0'){
                ++zero;
                oneZero += ones;
                ways += zeroOne;
            }
            else
            {
                ++ones;
                zeroOne += zero;
                ways += oneZero;
            }
        }

        return ways;
        
    }
}