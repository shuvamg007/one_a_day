class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        nodes = defaultdict(list)

        for x, y in edges:
            nodes[x].append(y)


        visited = set()

        @lru_cache(None)
        def check_cycle(node):
            nonlocal visited
            if node in visited:
                return 1

            visited.add(node)
            for n in nodes[node]:
                if check_cycle(n):
                    return 1
            visited.remove(node)

            return 0

                

        @lru_cache(None)
        def dfs(node):
            cnt = [0] * 26

            for i in nodes[node]:
                cnt = [max(cnt1, cnt2) for cnt1, cnt2 in zip(cnt, dfs(i))]

            cnt[ord(colors[node]) - ord('a')] += 1

            return cnt

        for i in range(len(colors)):
            if check_cycle(i):
                return -1

        return max(max(dfs(node)) for node in range(len(colors)))

