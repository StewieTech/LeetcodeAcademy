from typing import Optional


class ListNode:
    def __init__( self, val=0, next=None) :
        self.val=val;
        self.next=next;

    def __str__(self):
        # Custom __str__ method to print the list nodes
        result = []
        node = self
        while node:
            result.append(str(node.val))
            node = node.next
        return " -> ".join(result)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None;current
        current = head ;
        while current:
            current.next, previous, current = previous, current, current.next;
        return previous;

def main():
    head = ListNode(0);
    head.next = ListNode(1);
    head.next.next = ListNode(2);
    head.next.next.next = ListNode(3);

    print(Solution().reverseList(head))

if __name__ == "__main__":
    main();
