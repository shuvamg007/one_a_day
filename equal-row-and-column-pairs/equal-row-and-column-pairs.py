class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def check(row, col):
            for i in range((n//2)+1):
                if grid[row][i] != grid[i][col] or grid[row][n-i-1] != grid[n-i-1][col]:
                    return False

            return True

        count = 0
        for i in range(n):
            for j in range(n):
                if grid[i][0] == grid[0][j] and check(i, j):
                    print(i, j)
                    count += 1

        return count