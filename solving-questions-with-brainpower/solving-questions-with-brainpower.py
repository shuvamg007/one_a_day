class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @lru_cache(None)
        def recursion(idx: int) -> int:
            if idx >= n:
                return 0
            val, skip = questions[idx]
            return max(recursion(idx + 1), val + recursion(idx + skip + 1))

        return recursion(0)