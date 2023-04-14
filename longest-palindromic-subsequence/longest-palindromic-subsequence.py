class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def rec(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            if s[i] == s[j]:
                return 2 + rec(i+1, j-1)

            else:
                return max(rec(i, j-1), rec(i+1, j))

        return rec(0, len(s)-1)
