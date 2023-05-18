class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        exclude = set()
        for a, b in edges:
            exclude.add(b)

        return set(range(n)).difference(exclude)
