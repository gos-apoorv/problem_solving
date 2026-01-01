class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0 
        self.n = n


    def move(self, row: int, col: int, player: int) -> int:
        
        step = 1 if player == 1 else -1
        
        self.row[row] += step
        self.col[col] += step

        if row == col:
            self.diag += step

            if self.diag == self.n:
                return 1
            elif self.diag == -self.n:
                return 2
        
        if self.n - col ==  row + 1:
            self.anti_diag += step

            if self.anti_diag == self.n:
                return 1
            elif self.anti_diag == -self.n:
                return 2
        

        if self.row[row] == self.n or self.col[col] == self.n:
            return 1

        if self.row[row] == -self.n or self.col[col] == -self.n:
            return 2
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)