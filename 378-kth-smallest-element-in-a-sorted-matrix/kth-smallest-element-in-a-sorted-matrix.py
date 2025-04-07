class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        for i in range(1,len(matrix)):
           matrix[0] =  matrix[0]+matrix[i]
        matrix[0].sort()
        return matrix[0][k-1]