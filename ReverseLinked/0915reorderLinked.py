from typing import Optional


class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val= val
        self.next = next

    def __str__(self) -> str:
        result = [];
        current = self;
        while (current) :
            result.append(str(current.val));
            current = current.next;
        return "-> ".join(result);

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head;
        fast = head.next;
        while (fast and fast.next):
            slow = slow.next;
            fast = slow.next.next ;

        second = slow.next;
        slow.next = None;
        prev  = None;
        while (second):
            second.next, prev, second = prev, second, second.next;
            
        
        first = head;
        second = prev;
        while (second) :
            first.next, first = second, first.next;
            second.next, second = first, second.next;

    
