class Solution {
    public int minimumKeypresses(String s) {
        // Create array of all char to store its occurences
        int[] seq = new int[26];

        for(char c: s.toCharArray()){
            seq[c - 'a']++;
        }
        // Sort the array
        Arrays.sort(seq);
        
        int res =0;

        for(int i=25; i >=0; i--){
            if(i > 16 ){
                res += seq[i];  // For first chars in keyboard
            } else if (i > 7 && i <=16){
                res += seq[i]*2; // For second chars in keyboard
            } else {
                res += seq[i]*3; // For third chars in keyboard
            }
        }

        return res;
    }
}