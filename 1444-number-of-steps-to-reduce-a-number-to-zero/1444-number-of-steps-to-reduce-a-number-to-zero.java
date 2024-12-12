class Solution {
    public int numberOfSteps(int num) {
        int steps=0;

        while(num>0){
            // Bitwise operation to check if number if odd
            if( (num & 1) != 0){
                num--;
            }
            else{
                num = num>>1;
            }
            steps++;
        }

        return steps;
    }
}