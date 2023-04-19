# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        def traverse(node, prev, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            if node is None:
                return
            traverse(node.left, 0, (0 if prev != 1 else depth + 1))
            traverse(node.right, 1, (0 if prev != 0 else depth + 1))

        traverse(root, -1, 0)

        return max_depth
