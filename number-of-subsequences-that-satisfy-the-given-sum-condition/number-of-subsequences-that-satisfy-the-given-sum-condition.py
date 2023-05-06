class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        sol = 0
        nums = sorted(nums)
        while l <= r:
            if nums[r] <= target - nums[l]:
                sol += pow(2, (r-l), 1000000007)
                sol %= (10**9 + 7)
                l += 1
            else:
                r -= 1

        return sol