class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        target = set(range(1, n+1))
        
        for i in range(n):
            row_set = set()
            col_set = set()
            for j in range(n):
                row_set.add(matrix[i][j])
                col_set.add(matrix[j][i])
            if row_set != target or col_set != target:
                return False
        return True