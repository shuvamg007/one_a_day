class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @lru_cache(None)
        def recursion(pl, pos, m):
            if pos == n:
                return 0

            res = float('inf') if pl == 1 else -1
            sum_val = 0
            for i in range(1, min(2*m, n-pos) + 1):
                sum_val += piles[pos+i-1]
                if pl == 0:
                    res = max(res, sum_val + recursion(1, pos+i, max(m, i)))
                else:
                    res = min(res, recursion(0, pos+i, max(m, i)))

            return res

        return recursion(0, 0, 1)