class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        tot = 0
        for i in range(m):
            tot += (mat[i][i] + mat[i][m-i-1])

        if m % 2:
            tot -= mat[m//2][m//2]

        return tot
