class Solution {
    public int kthFactor(int n, int k) {
        // Create new ArrayList
        ArrayList<Integer> factor_list = new ArrayList<>();

        // Loop through all numbers from 1 to n to get the factors
        for(int num=1;num<=n;num++){
            if(n%num == 0)
            {
                factor_list.add(num);

                if(factor_list.size()==k){
                    return num;
                }
            }

        }

        return -1;

        
    }
}