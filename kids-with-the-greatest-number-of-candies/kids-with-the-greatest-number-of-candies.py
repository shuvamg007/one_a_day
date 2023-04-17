class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        op = [False] * len(candies)
        
        for idx, i in enumerate(candies):
            if i + extraCandies >= max_val:
                op[idx] = True

        return op
