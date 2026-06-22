class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # first find the row

        left = 0
        right = len(matrix) - 1
        lm = 0
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target:
                lm = mid
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(matrix[lm]) - 1
        while left <= right:
            mid = (left + right ) // 2
            if matrix[lm][mid] == target:
                return True
            if target < matrix[lm][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False

