class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        arr_len = len(heights) - 1

        max_height = 0
        ocean_view = []
        for pos in range(arr_len, -1, -1):

            if heights[pos] > max_height:
                ocean_view.append(pos)
            max_height = max(max_height, heights[pos])
        
        ocean_view.reverse()

        return ocean_view