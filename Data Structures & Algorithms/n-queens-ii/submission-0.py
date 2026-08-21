class Solution:
    def totalNQueens(self, n: int) -> int:

        count = 0
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isSafe(row, col):

            for i in range(row):
                if board[i][col] == "Q":
                    return False

            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def solve(row):

            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):

                if isSafe(row, col):

                    board[row][col] = 'Q'

                    solve(row + 1)

                    board[row][col] = '.'

        solve(0)

        return count