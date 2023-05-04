class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r, d = collections.deque(), collections.deque()

        for idx, i in enumerate(senate):
            if i == 'R':
                r.append(idx)
            else:
                d.append(idx)

        while d and r:
            _r, _d = r.popleft(), d.popleft()
            if _r < _d:
                r.append(n + _r)
            else:
                d.append(n + _d)

        return 'Radiant' if len(r) else 'Dire'
                