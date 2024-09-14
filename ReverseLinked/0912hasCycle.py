from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head ;
        while (fast and fast.next) :
            slow = slow.next ;
            fast = fast.next.next ;
            if (slow == fast) :
                return True
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
            
        return False
