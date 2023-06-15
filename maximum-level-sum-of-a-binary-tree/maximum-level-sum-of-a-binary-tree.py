# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        max_sum, ans = -float('inf'), 1
        lv = 0

        while q:
            lenq = len(q)
            lv += 1
            curr_sum = 0
            for _ in range(lenq):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = lv

        return ans