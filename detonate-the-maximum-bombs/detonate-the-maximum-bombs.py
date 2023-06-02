class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        neighbors = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dist = (x1 - x2)**2 + (y1 - y2)**2
                if dist <= r1**2:
                    neighbors[i].append(j)

                if dist <= r2**2:
                    neighbors[j].append(i)

        max_len = 0
        for i in range(n):
            visited = set()
            q = collections.deque()
            q.append(i)
            
            while q:
                lenq = len(q)
                for _ in range(lenq):
                    top = q.popleft()
                    if top not in visited:
                        visited.add(top)
                        for x in neighbors[top]:
                            q.append(x)

            max_len = max(max_len, len(visited))

        return max_len

