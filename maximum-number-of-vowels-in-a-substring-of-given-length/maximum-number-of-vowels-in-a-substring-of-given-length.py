class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        set_vow = set()
        max_len = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] in {'a', 'e', 'i', 'o', 'u'}:
                set_vow.add(r)
            if r - l == k:
                if l in set_vow: set_vow.remove(l) 
                l += 1

            max_len = max(max_len, len(set_vow))
            r += 1

        return max_len
