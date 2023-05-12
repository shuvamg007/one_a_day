class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n

        def recursion(idx: int) -> int:
            if idx >= n:
                return 0
            if dp[idx]:
                return dp[idx]

            val, skip = questions[idx]
            dp[idx] = max(recursion(idx + 1), val + recursion(idx + skip + 1))

            return dp[idx]

        return recursion(0)