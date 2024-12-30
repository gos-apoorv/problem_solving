class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        // Find the max candies amonst the kids i.e. in the arrays
        int maxCandies = 0;

        for(int candy: candies){
            maxCandies = Math.max(candy, maxCandies);
        }

        // Prepare the array to be returned
        List<Boolean> answer = new ArrayList<>();

        // Calculate the array by adding the current candies with extra ones and comparing it with maxCandies
        for(int candy: candies){
            answer.add(maxCandies<=(candy+extraCandies)?true:false);
        }

        return answer;
    }
}