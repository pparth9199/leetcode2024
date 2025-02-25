class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)* (len(mat[0])):
            return mat
        l = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                l.append(mat[i][j])
        newmat = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for i in range(r):
            for j in range(c):
                newmat[i][j] = l[k]
                k = k + 1
        return newmat