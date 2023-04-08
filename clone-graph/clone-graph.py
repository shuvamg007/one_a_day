"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node', visited=None) -> 'Node':
        if not visited:
            visited = dict()
        if not node or node in visited:
            return

        n_node = Node()
        n_node.val = node.val

        visited[node] = n_node
        for i in node.neighbors:
            if i not in visited:
                visited[i] = self.cloneGraph(i, visited)
            n_node.neighbors.append(visited[i])

        return n_node