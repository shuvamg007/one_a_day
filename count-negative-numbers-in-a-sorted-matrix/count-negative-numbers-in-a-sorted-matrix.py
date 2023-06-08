class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        end = -1
        count = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, end, -1):
                if grid[i][j] < 0:
                    count += 1
                else:
                    break

            end = j - 1
            if j == m - 1:
                return count

        return count