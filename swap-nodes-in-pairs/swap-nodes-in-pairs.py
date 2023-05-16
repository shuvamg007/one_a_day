# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = slow = fast = head
        fast = fast.next
        change = 1

        while slow.next:
            if not change:
                prev.next = fast

            slow.next = fast.next
            fast.next = slow
            prev = slow

            if change:
                head = fast
                change = 0

            if slow.next:
                slow = slow.next
            if slow.next:
                fast = slow.next


        return head