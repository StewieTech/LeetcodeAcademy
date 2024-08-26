class Solution:
    def searchMatrixNotBinary(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return target in row;
        return False ;

