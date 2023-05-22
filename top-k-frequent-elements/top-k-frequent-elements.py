class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for i in nums:
            hmap[i] += 1
        sorted_hmap = sorted(hmap, key=hmap.get, reverse=True)

        return sorted_hmap[:k]