class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        if rows == 0:
            return
        cols = len(board[0])

        # i, j = 0, 0
        for i in range(len(board)):
            if board[i][0] == "O":
                self.util(board, i, 0, rows, cols)
            if board[i][cols-1] == "O":
                self.util(board, i, cols-1, rows, cols)
                
        for i in range(len(board[0])):
            if board[0][i] == "O":
                self.util(board, 0, i, rows, cols)
            if board[rows-1][i] == "O":
                self.util(board, rows-1, i, rows, cols-1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                #print(i,j)
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "done":
                    board[i][j] = "O"
                              
                    
    def util(self, board, sr, sc, rows, cols):
        #print(sr, sc)
        if sr < 0 or sc < 0 or sr >= rows or sc >= cols or board[sr][sc] != "O":
            return 
        
        board[sr][sc] = "done"
        #print(sr,sc)
        self.util(board, sr+1, sc,  rows, cols)
        self.util(board, sr-1, sc,  rows, cols)
        self.util(board, sr, sc+1,  rows, cols)
        self.util(board, sr, sc-1,  rows, cols)
        #print(board)