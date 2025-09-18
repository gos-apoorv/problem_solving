class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        i = 0
        j = 0
        rows = len(mat)
        cols = len(mat[0])

        result = []
        direction = True
        while i < rows and j < cols:
            # print(i, j, direction)
            result.append(mat[i][j])

            if direction:
                if i == 0 and j < cols - 1:
                    direction = False
                    j += 1
                elif j == cols - 1:
                    direction = False
                    i += 1
                else:
                    i -= 1
                    j += 1
            else:
                if j == 0 and i < rows - 1:
                    direction = True
                    i += 1
                elif i == rows - 1:
                    direction = True
                    j += 1
                else:
                    i += 1
                    j -= 1
            
        
        return result



