class Solution:
    def minInsertions(self, s: str) -> int:
        l, r = 0, len(s) - 1

        @lru_cache(None)
        def get_min(l, r):
            if l >= r:
                return 0
            if s[l] == s[r]:
                return get_min(l+1, r-1)
            else:
                return 1 + min(get_min(l+1, r), get_min(l, r-1))

        return get_min(l, r)