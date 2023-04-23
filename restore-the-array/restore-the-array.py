class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        @lru_cache(None)
        def recursion(start: int):
            # base case
            if start == len(s):
                return 1

            if s[start] == '0':
                return 0

            count = 0
            
            # recursion
            for i in range(start, len(s)):
                if int(s[start: i+1]) > k:
                    break
                count += recursion(i+1)
            return count % (10**9 + 7)


        return recursion(0)
