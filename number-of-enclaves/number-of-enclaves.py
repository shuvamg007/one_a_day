class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set() 
        hmap = dict()

        def dfs(i, j):
            nonlocal visited, grid
            if not 0 <= i < n or not 0 <= j < m:
                return
            elif not grid[i][j]:
                return 
            else:
                grid[i][j] = 0

            visited.add((i, j))
            
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                a, b = x+i, y+j
                if (a, b) not in visited:
                    dfs(a, b)

        for i in range(n):
            for j in range(m):
                if i in [0, n-1] or j in [0, m-1]:
                    dfs(i, j)

        return sum([sum(x) for x in grid])