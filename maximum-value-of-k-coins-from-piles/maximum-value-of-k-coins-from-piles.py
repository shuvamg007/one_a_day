class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def pick(i, k):
            if i == 0:
                return 0

            curr_sum = 0
            max_val = 0
            for idx in range(min(len(piles[i-1]), k) + 1):
                if idx > 0:
                    curr_sum += piles[i-1][idx-1]
                max_val = max(max_val, pick(i-1, k-idx) + curr_sum)
            return max_val

        return pick(len(piles), k)
