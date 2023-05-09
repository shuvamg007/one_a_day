class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        m, n = len(matrix[0]), len(matrix)
        op = []

        jstep, istep = 1, 1
        while True:
            for _ in range(m):
                if matrix[i][j] > -101:
                    op.append(matrix[i][j])
                    matrix[i][j] = -101
                j += jstep
            j -= jstep

            for _ in range(n):
                if matrix[i][j] > -101:
                    op.append(matrix[i][j])
                    matrix[i][j] = -101
                i += istep
            i -= istep

            jstep *= -1
            istep *= -1
            j += jstep


            m -= 1
            n -= 1
            if m == 0 or n == 0:
                break 

        return op
