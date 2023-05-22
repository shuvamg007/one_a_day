class Solution:
    def partitionString(self, s: str) -> int:
        l, r = 0, 0
        hmap = defaultdict(int)
        count = 0

        while r < len(s):
            if hmap[s[r]] > 0:
                count += 1
                hmap = defaultdict(int)
                l = r
            hmap[s[r]] += 1
            r += 1

        if l != r:
            count += 1

        return count