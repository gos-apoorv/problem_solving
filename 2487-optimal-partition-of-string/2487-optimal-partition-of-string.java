import java.io.*;
import java.util.Arrays;

class Solution {
    public int partitionString(String s) {

        int count = 1;
        int substring = 1;
        int[] lastSeen = new int[26];
        char c;

        for(int i =1; i<=s.length();i++)
        {
            c = s.charAt(i-1);
            // This ensures that the new substring is accounted
            if(lastSeen[((int) c)-((int) 'a')] >= substring)
            {
                count += 1;
                substring = i;
            }
            lastSeen[((int) c)-((int) 'a')] = i;
        }

        return count;
    }
}