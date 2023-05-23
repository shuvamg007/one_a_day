class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        
    def bin_insert(self, num):
        l, r = 0, len(self.nums)
        while l < r:
            mid = (l+r) // 2
            if num > self.nums[mid]:
                l = mid + 1
            else:
                r = mid

        self.nums.insert(l, num)

    def add(self, val: int) -> int:
        self.bin_insert(val)
        return self.nums[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)