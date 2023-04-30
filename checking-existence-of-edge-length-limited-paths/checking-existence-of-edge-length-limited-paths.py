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
            self.rank[root_y] += 1

        return True

        
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        sorted_edges = sorted(edgeList, key=lambda x: x[2])
        sorted_queries = sorted([(w, u, v, i) for i, (u, v, w) in enumerate(queries)])
        counter = 0

        ans = [0] * len(queries)

        uf = UnionFind(n)

        for w, u, v, i in sorted_queries:
            while counter < len(sorted_edges):
                u_e, v_e, w_e = sorted_edges[counter]
                if w_e < w:
                    counter += 1
                    uf.union(u_e, v_e)
                else: break
            ans[i] = uf.find(u) == uf.find(v)

        return ans


