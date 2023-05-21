class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        memo = dict()
        n = len(grid)

        def assign_set(x, y, visited):
            if not 0 <= x < n or not 0 <= y < n or not grid[x][y]:
                return
            visited.add((x, y))
            for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                _x, _y = x+i, y+j
                if (_x, _y) not in visited:
                    assign_set(_x, _y, visited)

            return visited

        def dfs(x, y, visited, sets, idx):
            nonlocal memo
            if not 0 <= x < n or not 0 <= y < n:
                return float('inf')
            if grid[x][y]:
                if (x, y) in sets:
                    return 0
                return float('inf')
            if (x, y, idx) in memo:
                return memo[(x, y, idx)]
            min_dist = float('inf')
            visited.add((x, y))
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _x, _y = x+i, y+j
                if (_x, _y) not in visited:
                    min_dist = min(min_dist, 1 + dfs(_x, _y, visited, sets, idx))

            visited.remove((x, y))
            memo[(x, y, idx)] = min_dist
            return min_dist

        min_res = float('inf')
        visited = None
        for i in range(n):
            for j in range(n):
                if grid[i][j] and not visited:
                    set_1 = assign_set(i, j, set())
                    visited = set_1.copy()

                elif grid[i][j] and (i, j) not in visited:
                    set_2 = assign_set(i, j, set())
                    break

        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    dist_1 = dfs(i, j, set(), set_1, 1)
                    dist_2 = dfs(i, j, set(), set_2, 2)
                    min_res = min(min_res, dist_1 + dist_2)
        # print(min_res)
        return min_res - 1