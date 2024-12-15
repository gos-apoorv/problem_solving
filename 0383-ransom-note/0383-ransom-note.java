class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

        // Return of lenght of magazine is smaller than ransomNote
        if(ransomNote.length() > magazine.length())
        {
            return false;
        }
        
        //  Create a new hashmap
        HashMap<Character, Integer> magazineHashMap = new HashMap<>();
        
        // Fill the hashmap with frequency of magazine
        for(int i=0;i<magazine.length();i++){
            char c = magazine.charAt(i);

            int currentCount =  magazineHashMap.getOrDefault(c, 0);
            
            magazineHashMap.put(c, currentCount + 1);
        }

        // Check magazineHashMap for all letter in ransomNote
        for(int j=0; j < ransomNote.length(); j++)
        {
            char t = ransomNote.charAt(j);

            int currentOccurence = magazineHashMap.getOrDefault(t, 0);

            if(currentOccurence==0){
                return false;
            }
            else{
                magazineHashMap.put(t, currentOccurence-1);
            }
        }

        return true;
    }
}