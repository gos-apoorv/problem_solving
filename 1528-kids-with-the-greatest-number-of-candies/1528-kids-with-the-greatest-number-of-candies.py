class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # Find the max_candies in the array
        max_candies = 0
        for candy in candies:
            max_candies = max(max_candies, candy)

        result = []

        # Calcuate the boolena array by comparing the sum of current candy and extra_candies with the max_candies 
        for candy in candies:
            result.append(True if extraCandies + candy >= max_candies else False )

        return result