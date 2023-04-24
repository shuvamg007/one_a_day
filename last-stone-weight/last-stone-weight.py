class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in stones:
            heapq.heappush(heap, -i)

        while heap:
            if len(heap) == 1:
                return -heap[0]
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            res = y - x
            if res:
                heapq.heappush(heap, -res)


        return 0
