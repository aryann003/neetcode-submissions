class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

         
        for i in range(n):
            start = matrix[i][0]
            end = matrix[i][-1]
            
            if target >= start and  target <= end:
                left = 0
                right = m
                while left <= right:
                    mid = left + (right-left)//2

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        right = mid-1
                    else:
                        left = mid+1
                return False

            else:
                continue

        return False