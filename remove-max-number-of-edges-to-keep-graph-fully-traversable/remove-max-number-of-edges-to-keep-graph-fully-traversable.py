class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        sorted_edges = sorted(edges, key=lambda x: -x[0])
        
        uf_a = UnionFind(n)
        uf_b = UnionFind(n)
        count = 0

        for edge in sorted_edges:
            _type, u, v = edge
            u -= 1
            v -= 1

            if _type == 3:
                conn_a = uf_a.union(u, v)
                conn_b = uf_b.union(u, v)
                if not conn_a and not conn_b:
                    count += 1

            elif _type == 2:
                if not uf_b.union(u, v):
                    count += 1

            elif _type == 1:
                if not uf_a.union(u, v):
                    count += 1

        root_a, root_b = uf_a.find(0), uf_b.find(0)

        for i in range(1, n):
            if uf_a.find(i) != root_a or uf_b.find(i) != root_b:
                return -1

        return count