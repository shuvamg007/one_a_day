class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        count = 0
        
        @lru_cache(None)
        def recursive(tot, mems, k):
            if k == len(group):
                if tot >= minProfit:
                    return 1
                return 0
            
            count = 0
            if mems + group[k] <= n:
                count += recursive(min(minProfit, tot + profit[k]), mems + group[k], k+1)
            count += recursive(tot, mems, k+1)

            return count

        return recursive(0, 0, 0) % (10**9+7)
