class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                l.append(mat[i][j])
        newmat = [[0 for _ in range(c)] for _ in range(r)]
        if len(l) < r*c:
            return mat
        k = 0
        for i in range(r):
            for j in range(c):
                newmat[i][j] = l[k]
                k = k + 1
        if k < len(l):
            return mat
        return newmat