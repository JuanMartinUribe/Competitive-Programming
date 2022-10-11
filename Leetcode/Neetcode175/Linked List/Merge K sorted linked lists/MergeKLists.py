# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        prev = ListNode(-1)
        h = []
        heapq.heapify(h)
        for head in lists:
            while head:
                heapq.heappush(h,head.val)
                head = head.next
        ans = prev
        while h:
            prev.next = ListNode(heapq.heappop(h))
            prev = prev.next      
        return ans.next