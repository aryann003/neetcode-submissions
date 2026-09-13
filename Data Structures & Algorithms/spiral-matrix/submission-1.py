class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        result = []

        srow = 0
        erow = m - 1
        scol = 0
        ecol = n - 1

        while srow <= erow and scol <= ecol:

            # left -> right
            for j in range(scol, ecol + 1):
                result.append(matrix[srow][j])

            # top -> bottom
            for i in range(srow + 1, erow + 1):
                result.append(matrix[i][ecol])

            # right -> left
            for j in range(ecol - 1, scol - 1, -1):
                if srow == erow:
                    break
                result.append(matrix[erow][j])

            # bottom -> top
            for i in range(erow - 1, srow, -1):
                if scol == ecol:
                    break
                result.append(matrix[i][scol])

            srow += 1
            scol += 1
            erow -= 1
            ecol -= 1

        return result
