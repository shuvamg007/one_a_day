class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts)
        memo = dict()

        def recursive(start, end, cuts):
            nonlocal memo
            if not len(cuts):
                return 0

            if (start, end) in memo:
                return memo[(start, end)]

            min_cost = float('inf')
            for idx in range(len(cuts)):
                cut = cuts[idx]
                # new_cuts = cuts[:idx] + cuts[idx+1:]
                min_cost = min(min_cost, end - start + recursive(start, cut, cuts[:idx]) + recursive(cut, end, cuts[idx+1:]))
                # print(start, end, recursive(0, cut, cuts[:idx]), recursive(cut, n, cuts[idx+1:]))

            memo[(start, end)] = min_cost
            return min_cost

        min_cost = float('inf')
        for idx in range(len(cuts)):
            cut = cuts[idx]
            # new_cuts =  + 
            min_cost = min(min_cost, n + recursive(0, cut, cuts[:idx]) + recursive(cut, n, cuts[idx+1:]))
            # print(n, recursive(0, cut, cuts[:idx]), recursive(cut, n, cuts[idx+1:]))
        return min_cost
