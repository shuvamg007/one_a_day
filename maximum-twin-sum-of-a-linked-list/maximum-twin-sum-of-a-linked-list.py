# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = ListNode(slow.val)

        while fast:
            fast = fast.next.next
            temp = prev
            prev = slow
            slow = slow.next
            prev.next = temp
        
        max_val = 0
        while slow:
            max_val = max(max_val, slow.val+prev.val)
            slow = slow.next
            prev = prev.next

        return max_val