class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        counter = 1
        x, y = 0, 0

        def fill_mat(start, end, inc, axis):
            nonlocal mat, x, y, counter
            if axis == 0:
                for i in range(start, end, inc):
                    if not mat[x][i]:
                        y = i
                        mat[x][i] = counter
                        counter += 1

            elif axis == 1:
                for i in range(start, end, inc):
                    if not mat[i][y]:
                        x = i
                        mat[i][y] = counter
                        counter += 1


        for _ in range(n):
            fill_mat(0, n, 1, 0)
            fill_mat(0, n, 1, 1)
            n -= 1

            fill_mat(n, -1, -1, 0)
            fill_mat(n, -1, -1, 1)

        return mat
