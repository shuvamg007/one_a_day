class Solution:
    def trap(self, height: List[int]) -> int:
        water = []

        left = 0
        for h in height:
            left = max(left, h)
            water.append(left)

        i = len(water) - 1
        right = 0
        for h in reversed(height):
            right = max(right, h)
            totWater = min(water[i], right)
            water[i] = totWater - h
            i -= 1

        return sum(water)