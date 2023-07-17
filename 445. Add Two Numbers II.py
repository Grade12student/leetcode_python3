# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create stacks to store digits of the two numbers
        s1, s2 = [], []
        # Push digits of l1 into stack1
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        # Push digits of l2 into stack2
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        # Variables to keep track of carry and the resulting linked list
        carry = 0
        res = None
        # Calculate the sum digit by digit
        while s1 or s2 or carry:
            # Calculate the sum of the current digits and carry
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            # Create a new node with the sum digit
            node = ListNode(carry % 10)
            node.next = res
            res = node
            # Update the carry
            carry //= 10
        return res
