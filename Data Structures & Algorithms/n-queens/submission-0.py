class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[]

        for i in range(n):
            board.append([])
            for j in range(n):
                board[i].append('.')

        result = []

        def isSafe(row,col):

            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            i = row-1
            j = col-1

            while i >= 0 and j>= 0:
                if board[i][j] == 'Q':
                    return False
                i = i-1
                j = j-1

            i = row-1
            j = col+1

            while i>=0 and j<n:
                if board[i][j] == "Q":
                    return False
                i = i-1
                j = j+1

            return True

        def solve(row):
            if row == n:
                ans = []
                for i in board:
                    ans.append("".join(i))
                result.append(ans)
                return
            
            for col in range(n):
                if isSafe(row,col):
                    board[row][col] = 'Q'
                    solve(row+1)
                    board[row][col] = '.'
            
        solve(0)
        return result

            


