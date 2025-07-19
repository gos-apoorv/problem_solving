class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # print(mat)
        for col in range(m - 1, -1, -1):
            for row in range(n - 1, -1, -1):

                if col == m - 1 and row == n - 1:
                    pass
                elif col == m - 1 and row < n - 1:
                    grid[col][row] = grid[col][row] + grid[col][row + 1]
                elif row == n - 1 and col < m - 1:
                    grid[col][row] = grid[col][row] + grid[col + 1][row]
                else:
                    grid[col][row] = grid[col][row] + min(grid[col + 1][row], grid[col][row + 1])
                # print(mat)

        
        # print(mat)
        return grid[0][0]