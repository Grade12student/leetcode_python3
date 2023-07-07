# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        # Create a pointer to the current node in the merged list
        cur = dummy
        # Traverse both lists simultaneously
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2
            # Connect the smaller value to the merged list
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        # Connect the remaining nodes of list1 or list2, if any
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        # Return the head of the merged list
        return dummy.next
