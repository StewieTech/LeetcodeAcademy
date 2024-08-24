from typing import Optional


class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val;
        self.next= next;
    
    def __str__ (self):
        result = [];
        current = self;
        while (current):
            result.append(str(current.val));
            current = current.next;
        return "->".join(result);


class Solution :
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        
        current = head ;
        tail = None;
        while (current):
            current.next, tail, current = tail, current, current.next;
        print("tail: ")
        print(tail);
        
        counter: int = 0 ;
        while (tail):
            tail = tail.next
            if (counter == n):
                tail = tail.next.next;
            counter += 1;

        prev = None
        while (tail):
            tail.next, prev, tail = prev, tail, tail.next;
        return tail ;

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = left = ListNode(0, head)
        right = head
        for _ in range(n): right = right.next
        while right: left, right = left.next, right.next
        left.next = left.next.next; return dummy.next


def main():
    head = ListNode(1);
    head.next = ListNode(2);
    head.next.next = ListNode(3);
    head.next.next.next = ListNode(4);

    print(Solution().removeNthFromEnd(head,2));



if __name__ == "__main__":
    main();

