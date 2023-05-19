class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        hmap = defaultdict(set)
        
        def dfs(n, sets):
            nonlocal visited, hmap
            if n in visited:
                if n not in hmap[sets]:
                    return False
                return True

            hmap[sets].add(n)
            visited.add(n)

            op = True
            for v in graph[n]:
                op = op and dfs(v, 1-sets)

            return op

        for i in range(len(graph)):
            if i not in visited:
                if not dfs(i, 0):
                    return False

        return True