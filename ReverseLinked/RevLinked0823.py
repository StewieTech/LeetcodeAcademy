
from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val; 
        self.next = next;

    def __str__(self):
        result = []
        current = self;
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None;
        current = head;
        # while current:
        #     current.next , prev = prev, current;
        # return prev
        while current:
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        return prev




def main():
    head = ListNode(0);
    head.next = ListNode(1);
    head.next.next = ListNode(2);
    head.next.next.next = ListNode(3);
    print(Solution().reverseList(head));

if __name__ == "__main__":
    main();