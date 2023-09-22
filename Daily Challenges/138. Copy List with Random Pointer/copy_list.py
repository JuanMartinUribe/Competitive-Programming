"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lookup = {}
        ans = head
        while head:
            lookup[head] = Node(head.val)
            head = head.next
        for og_node,copy in lookup.items():
            copy.next = lookup[og_node.next] if og_node.next else None
            copy.random = lookup[og_node.random] if og_node.random else None
        return lookup[ans] if ans else None

