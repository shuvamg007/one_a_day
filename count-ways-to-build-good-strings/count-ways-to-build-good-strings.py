class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # @lru_cache(None)
        # def recursion(length):
        #     count = 0
        #     if low <= length <= high:
        #         count += 1

        #     if length > high:
        #         return 0

        #     count += recursion(length + zero)
        #     count += recursion(length + one)

        #     return count
        
        # return recursion(0) % (10**9 + 7)


        dp = [0] * (high + 1)
        dp[0] = 1
        mod = (10**9 + 7)
        for i in range(high+1):
            dp[i] += (dp[i - one] + dp[i - zero]) % mod

        return sum(dp[low:high+1]) % mod
