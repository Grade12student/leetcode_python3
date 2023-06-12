# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length +=1
            cur = cur.next
        kth_start = head
        for _ in range(k-1):
            kth_start = kth_start.next
        kth_end = head
        for _ in range(length-k):
            kth_end = kth_end.next
        kth_start.val, kth_end.val = kth_end.val, kth_start.val
        return head