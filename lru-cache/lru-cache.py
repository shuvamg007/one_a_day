class LRUCache:

    def __init__(self, capacity: int):
        self.counter = 0
        self.cap = capacity
        self.hmap = dict()
        self.q = collections.deque() 

    def get(self, key: int) -> int:
        if key in self.hmap:
            val = self.hmap[key][0]
            self.hmap[key] = (val, self.counter)
            self.q.append((key, self.counter))

            self.counter += 1

            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hmap:
            while len(self.hmap) >= self.cap:
                k, _counter = self.q.popleft()
                if _counter == self.hmap[k][1]:
                    del self.hmap[k]

        self.hmap[key] = (value, self.counter)
        self.q.append((key, self.counter))
        self.counter += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)