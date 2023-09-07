# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        prev = None
        nxt = None
        i = 0
        rev = []
        cur = head
        while cur:
            if i==left-2:
                prev = cur
            elif i==right:
                nxt = cur
            elif left-1<=i<=right-1:
                rev.append(cur)
            cur = cur.next
            i+=1
        rev[0].next = nxt
        for i,node in enumerate(rev[1:]):
            node.next = rev[i]
        if prev:
            prev.next = rev[-1]
        return head if left>1 else rev[-1]
