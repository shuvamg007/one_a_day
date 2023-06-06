class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        hset = set()
        for i in range(1, len(arr)):
            hset.add(arr[i] - arr[i-1])
            if len(hset) > 1:
                return False

        return True