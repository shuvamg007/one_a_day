class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        op, visited = set(), set()
        def dfs(n):
            if n in visited:
                if n in op:
                    op.remove(n)
                return
            op.add(n)
            visited.add(n)

            for j in nodes[n]:
                if j in op:
                    op.remove(j)

                dfs(j)


        nodes = defaultdict(list)
        for x, y in edges:
            nodes[x].append(y)

        for i in range(n):
            dfs(i)

        return list(op)
