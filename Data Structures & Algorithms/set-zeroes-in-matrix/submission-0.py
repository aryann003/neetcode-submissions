class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rc = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = -1
                    rc.append([i,j])

        

        for k in rc:
            r = k[0]
            c = k[1]

            for i in range(0,len(matrix)):
                matrix[i][c] = 0
            for j in range(0,len(matrix[0])):
                matrix[r][j] = 0
        