from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                row_check = (num, "row", r)
                col_check = (num, "col", c)
                box_check = (num, "box", r // 3, c // 3)

                if row_check in seen or col_check in seen or box_check in seen:
                    return False

                seen.add(row_check)
                seen.add(col_check)
                seen.add(box_check)

        return True