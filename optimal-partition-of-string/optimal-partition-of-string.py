class Solution:
    def partitionString(self, s: str) -> int:
        l, r = 0, 0
        hmap = dict()
        count = 0

        while r < len(s):
            if s[r] in hmap:
                count += 1
                hmap = dict()
                l = r
            hmap[s[r]] = 1
            r += 1

        if l != r:
            count += 1

        return count