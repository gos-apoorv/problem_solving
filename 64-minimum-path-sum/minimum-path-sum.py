class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mat = [[0] * n for _ in range(m)]

        # print(mat)
        for col in range(m - 1, -1, -1):
            for row in range(n - 1, -1, -1):

                if col == m - 1 and row == n - 1:
                    mat[col][row] = grid[col][row]
                elif col == m - 1 and row < n - 1:
                    mat[col][row] = grid[col][row] + mat[col][row + 1]
                elif row == n - 1 and col < m - 1:
                    mat[col][row] = grid[col][row] + mat[col + 1][row]
                else:
                    mat[col][row] = grid[col][row] + min(mat[col + 1][row], mat[col][row + 1])
                # print(mat)

        
        # print(mat)
        return mat[0][0]