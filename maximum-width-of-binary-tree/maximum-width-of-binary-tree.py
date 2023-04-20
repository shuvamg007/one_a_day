# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()

        max_len = 0

        q.append((root, 1))

        while q:
            lenq = len(q)
            l = None
            for _ in range(lenq):
                popd, idx = q.popleft()
                if not l:
                    l = idx
                max_len = max(max_len, idx - l + 1)
                if popd.left:
                    q.append((popd.left, 2*idx - 1))
                if popd.right:
                    q.append((popd.right, 2*idx))
                
        return max_len