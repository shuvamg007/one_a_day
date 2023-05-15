# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len_list = 0
        start = head
        while start:
            start = start.next
            len_list += 1

        forward = backward = head

        len_list -= k
        while k>1:
            forward = forward.next
            k -= 1

        while len_list:
            backward = backward.next
            len_list -= 1
        
        forward.val, backward.val = backward.val, forward.val
        # forward.next, backward.next = backward.next, forward.next

        return head