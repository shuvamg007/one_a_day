class LRUCache:

    def __init__(self, capacity: int):
        self.map = dict()
        self.q = collections.deque()
        self.counter = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.map:
            val, countr = self.map[key]

            self.map[key] = (val, self.counter)
            self.q.append((key, self.counter))

            self.counter += 1
            return self.map[key][0]

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = (value, self.counter)
            self.q.append((key, self.counter))
            self.counter += 1

        else:
            while len(self.map) >= self.capacity:
                k, countr = self.q.popleft()
                if self.map[k][1] == countr:
                    del self.map[k]
            self.map[key] = (value, self.counter)
            self.q.append((key, self.counter))
            self.counter += 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)