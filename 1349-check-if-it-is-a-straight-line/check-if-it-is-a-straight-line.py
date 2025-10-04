class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        co_0 = coordinates[0]
        co_1 = coordinates[1]
        delta_x = co_1[0] - co_0[0]
        delta_y = co_1[1] - co_0[1]

        for n in range(1, len(coordinates)):
            diff_x = coordinates[n][0] - coordinates[n-1][0]
            diff_y = coordinates[n][1] - coordinates[n-1][1]

            if diff_x*  delta_y == delta_x * diff_y:
                continue
            else:
                return False
        
        return True
        