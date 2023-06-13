class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for idx, i in enumerate(manager):
            if i != -1:
                graph[i].append(idx)


        q = collections.deque()
        q.append((headID, 0))
        visited = set()
        maxTime = 0

        while q:
            lenq = len(q)
            for _ in range(lenq):
                head, time = q.popleft()
                if head not in visited:
                    if not informTime[head]:
                        maxTime = max(maxTime, time)
                    else:
                        for k in graph[head]:
                            q.append((k, time + informTime[head]))

                    visited.add(head)

        return maxTime
