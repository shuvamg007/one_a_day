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
        fz, fo = 1, 1
        for i in range(high+1):
            if i >= zero + one:
                dp[i] += dp[i - one] + dp[i - zero]
            else:
                if i >= zero:
                    dp[i] = dp[i - zero]
                    if not dp[i - zero] and fz:
                        dp[i] += 1
                        fz = 0
                if i >= one:
                    dp[i] += dp[i - one]
                    if not dp[i - one] and fo:
                        dp[i] += 1
                        fo = 0

            dp[i] %= (10**9 + 7)

        return sum(dp[low:high+1]) % (10**9 + 7)
