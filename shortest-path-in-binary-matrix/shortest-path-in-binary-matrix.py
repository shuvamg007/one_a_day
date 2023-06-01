class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = collections.deque()

        if grid[0][0] or grid[n-1][n-1]:
            return -1

        grid[0][0] = 1
        q.append((0, 0, 1))

        while q:
            x, y, d = q.popleft()
            if x == n-1 and y == n-1:
                return d

            for _x, _y in [(x-1, y-1), (x-1, y), (x-1, y+1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y-1), (x, y+1)]:
                if 0 <= _x < n and 0 <= _y < n and grid[_x][_y] == 0:
                    grid[_x][_y] = 1
                    q.append((_x, _y, d+1))

        return -1
