class Solution:
    def arraySign(self, nums: List[int]) -> int:
        counter = 0

        for i in nums:
            if i < 0:
                counter += 1
            elif i == 0:
                return 0

        return 1 if counter % 2 == 0 else -1