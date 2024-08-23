

from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val;
        self.next = next;

class Solution:
    def reorderList(self, head: Optional[ListNode] ) -> None :
        slow, fast = head, head.next;
        while fast and fast.next:
            slow = slow.next;
            fast = fast.next.next;

        second = slow.next;
        prev = slow.next = None;
        while second:
            second.next, prev, second = prev, second, second.next;
        
        first, second = head, prev;
        while second:
            first.next, first = second, first.next;
            second.next, second = first, second.next;

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next: slow, fast = slow.next, fast.next.next
        prev, cur = None, slow.next; slow.next = None
        while cur: cur.next, prev, cur = prev, cur, cur.next
        first, second = head, prev
        while second: first.next, first, second.next, second = second, first.next, first, second.next

