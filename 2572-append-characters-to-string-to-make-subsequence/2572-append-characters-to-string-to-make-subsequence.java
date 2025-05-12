

import static java.lang.Integer.signum;

class Solution {
    public int appendCharacters(String s, String t) {

        int start = 0, t_pos = 0;

        while(start < s.length() && t_pos < t.length()){
            if(s.charAt(start)==t.charAt(t_pos)){
                t_pos ++;
            }
            start ++;
        }
        return t.length() - t_pos;
    }
}