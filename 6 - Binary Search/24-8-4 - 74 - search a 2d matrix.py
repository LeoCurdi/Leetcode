class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        - given: a sorted m x n integer matrix
        - find: whether a target is in the matrix

        - perform a binary search on the rows to get the target row, then binary search that row
        
        - time: logm + logn
        """
        # get number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])

        # binary search the rows
        top, bottom = 0, rows-1
        while top < bottom:
            middle = top + (bottom - top) // 2 + 1
            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else:
                top = middle

        # binary search target row
        left, right = 0, cols-1
        while left <= right:
            middle = left + (right - left) // 2
            if matrix[top][middle] > target:
                right = middle - 1
            elif matrix[top][middle] < target:
                left = middle + 1
            else:
                return True