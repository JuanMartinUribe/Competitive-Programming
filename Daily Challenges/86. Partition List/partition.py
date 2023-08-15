# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        smaller = []
        greater = []
        while head:
            if head.val<x:
                smaller.append(head)
            else:
                greater.append(head)
            head = head.next
        arr = smaller+greater
        ans = ListNode()
        ans.next = arr[0]
        for i,node in enumerate(arr):
            if i<len(arr)-1:
                node.next = arr[i+1]
            else:
                node.next = None
        return ans.next