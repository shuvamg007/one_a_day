class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo = [-1] * 2**(len(nums))
        def backtrack(mask, count):
            nonlocal memo

            if count * 2 == len(nums):
                return 0

            if memo[mask] != -1:
                return memo[mask]

            maxVal = 0
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if (mask >> i) & 1 == 1 or (mask >> j) & 1 == 1:
                        continue

                    newMask = mask | (1 << i) | (1 << j)

                    curr = (count + 1) * math.gcd(nums[i], nums[j])
                    rem = backtrack(newMask, count + 1)

                    maxVal = max(maxVal, curr + rem)

            memo[mask] = maxVal

            return memo[mask]


        return backtrack(0, 0)