class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        exclude = set()
        for a, b in edges:
            exclude.add(b)

        return [x for x in range(n) if x not in exclude]
