# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            while head:
                nxt =  head.next
                head.next = prev
                prev = head
                head = nxt
            return prev
        
        l1,l2 = reverse(l1),reverse(l2)
        l3 = ListNode()
        ans = l3
        rem = 0
        while l1 or l2:
            if l1 and l2:
                val = l1.val+l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val
                l1 = l1.next
            elif l2:
                val = l2.val
                l2 = l2.next
            l3.val = (val+rem)%10
            l3.next = ListNode() if l1 or l2 else None
            l3 = l3.next if l1 or l2 else l3
            rem = (val+rem)//10
        if rem:
            l3.next = ListNode(rem)
            l3 = l3.next
        return reverse(ans)
            