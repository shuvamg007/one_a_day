class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i, j = 1, n - 2
        lmax, rmax = height[0], height[n-1]

        ans = 0
        while i <= j:
            if lmax < height[i]:
                lmax = height[i]
            if rmax < height[j]:
                rmax = height[j]

            if lmax <= rmax:
                ans += (lmax - height[i])
                i += 1

            else:
                ans += (rmax - height[j])
                j -= 1

        return ans