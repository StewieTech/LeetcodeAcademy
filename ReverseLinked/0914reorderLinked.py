from typing import Optional


class ListNode: 
    def __init__ (self, val=0, next = None):
        self.val = val;
        self.next = next;

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head;
        while (fast and fast.next) :
            slow = slow.next;
            fast = fast.next.next;

        second = slow.next;
        slow = None;
        prev = None;
        while (second) : 
            second.next, prev, second = prev, second, second.next ;

        first = head;
        while (second):
            first.next, first = second, first.next ;
            second.next, second = first.next, second.next;

        
