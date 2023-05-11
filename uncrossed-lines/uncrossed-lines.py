class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        @lru_cache(None)
        def recursion(i, j):
            if i == n or j == m:
                return 0

            max_cost = 0
            if nums1[i] == nums2[j]:
                max_cost = max(max_cost, 1 + recursion(i+1, j+1))

            max_cost = max(max_cost, recursion(i+1, j))
            max_cost = max(max_cost, recursion(i, j+1))

            return max_cost

        return recursion(0, 0)