class SmallestInfiniteSet:

    def __init__(self):
        self.counter = 0
        self.heap = []
        self.hset = set()

    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.hset.remove(num)
            return num

        self.counter += 1
        return self.counter

    def addBack(self, num: int) -> None:
        if num <= self.counter and num not in self.hset:
            self.hset.add(num)
            heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)