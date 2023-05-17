# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = head
        n = 0
        while dummy: 
            n+=1
            dummy = dummy.next
        
        lookup = collections.defaultdict(int)
        i = 0 
        ans = 0
        while head:
            if i<=(n//2)-1:
                lookup[n-1-i] = (i,head.val)
            else:
                ans = max(ans,head.val+lookup[i][1])
            i+=1
            head=head.next
        return ans        
