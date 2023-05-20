# class Node:
#     def __init__(self, x):
#         self.parent = x
#         self.rank = 1
  
# class UnionFind:
#     def __init__(self, parents):
#         self.parents = parents

#     def find(self, x):
#         if self.find(x) != x:
#             return self.find(x.parent)
#         return x.parent

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        nodes = defaultdict(list)
        for idx, (i, j) in enumerate(equations):
            nodes[i].append((j, values[idx]))
            nodes[j].append((i, 1 / values[idx]))

        memo = dict()

        def dfs(a, z, visited):
            nonlocal memo
            if a == z:
                return 1

            # if (a, z) in memo:
            #     return memo[(a, z)]

            val = 1
            for x in nodes[a]:
                if x not in visited:
                    visited.add(x)
                    div = dfs(x[0], z, visited)
                    if div != 0:
                        val *= (x[1] * div)
                        visited.remove(x)
                        memo[(x[0], z)] = val
                        return val

                    else:
                        visited.remove(x)

            return 0


        op = []
        for a, b in queries:
            if a in nodes and b in nodes:
                res = dfs(a, b, set())
                op.append(-1 if res == 0 else res)
            else:
                op.append(-1)

        return op